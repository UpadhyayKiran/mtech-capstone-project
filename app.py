import json
import faiss
import fitz
import torch
import re
import math
import unicodedata
import pandas as pd
import streamlit as st
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from peft import PeftModel
from logger_utils import log_query_result


# =========================
# PATHS
# =========================
FAISS_INDEX_PATH = "vectorstore/faiss_index.index"
METADATA_PATH = "vectorstore/chunk_metadata.json"

EMBED_MODEL = "pritamdeka/S-PubMedBert-MS-MARCO"
BASE_MODEL = "BioMistral/BioMistral-7B"
ADAPTER_PATH = "qlora_biomistral_adapter"

DEFAULT_TOP_K = 3


st.set_page_config(
    page_title="Agentic Evidence-Based Clinical Research Assistant",
    page_icon="🧬",
    layout="wide",
)


# =========================
# LOADERS
# =========================
@st.cache_resource
def load_retrieval_components():
    index = faiss.read_index(FAISS_INDEX_PATH)

    with open(METADATA_PATH, "r", encoding="utf-8") as f:
        metadata = json.load(f)

    device = "cuda" if torch.cuda.is_available() else "cpu"
    embed_model = SentenceTransformer(EMBED_MODEL, device=device)

    return index, metadata, embed_model


@st.cache_resource
def load_finetuned_model():
    tokenizer = AutoTokenizer.from_pretrained(
        BASE_MODEL,
        use_safetensors=False
    )

    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    quant_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_compute_dtype=torch.float16,
        bnb_4bit_use_double_quant=True,
        bnb_4bit_quant_type="nf4",
    )

    base_model = AutoModelForCausalLM.from_pretrained(
        BASE_MODEL,
        quantization_config=quant_config,
        device_map="auto",
        use_safetensors=False,
    )

    model = PeftModel.from_pretrained(base_model, ADAPTER_PATH)
    model.eval()

    return tokenizer, model

# =========================
# TEXT CLEANING
# =========================
def clean_display_text(text):
    if not text:
        return ""

    text = str(text)
    text = unicodedata.normalize("NFKC", text)
    text = re.sub(r"[\x00-\x1F\x7F-\x9F]", "", text)
    text = text.replace("�", "").replace("\ufffd", "").replace("\x00", "")
    text = text.replace("­", "")
    text = re.sub(r"[□■]", "", text)

    noisy_patterns = [
        r"XSL\s*•?\s*FO\s*RenderX",
        r"page number not for citation purposes",
        r"DOI:\s*\S+",
        r"https?://\S+",
        r"\bRenderX\b",
    ]

    for pattern in noisy_patterns:
        text = re.sub(pattern, " ", text, flags=re.IGNORECASE)

    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"\s+([.,;:])", r"\1", text)
    text = re.sub(r"\.{2,}", ".", text)

    return text.strip()


def truncate_to_sentence(text, max_chars=1000):
    text = clean_display_text(text)

    if len(text) <= max_chars:
        return text

    truncated = text[:max_chars]
    last_end = max(
        truncated.rfind("."),
        truncated.rfind("?"),
        truncated.rfind("!")
    )

    if last_end > 250:
        return truncated[:last_end + 1].strip()

    return truncated.rsplit(" ", 1)[0].strip() + "..."

def generate_dynamic_summary(chunks):
    if not chunks:
        return "No relevant biomedical evidence was retrieved."

    summary_parts = []

    for chunk in chunks[:2]:
        text = clean_display_text(chunk.get("chunk_text", ""))

        text = truncate_to_sentence(text, 350)

        sentences = re.split(r'(?<=[.!?])\s+', text)

        if sentences:
            first_sentence = sentences[0].strip()

            if len(first_sentence.split()) > 6:
                summary_parts.append(first_sentence)

    if not summary_parts:
        return "Relevant biomedical evidence was retrieved and synthesized from the literature."

    summary = " ".join(summary_parts)

    summary = re.sub(r"\s+", " ", summary).strip()

    return summary

def get_terms(text):
    return set(
        w.lower()
        for w in re.findall(r"[a-zA-Z]+", str(text))
        if len(w) > 3
    )


# =========================
# AGENT STEP 1: QUERY UNDERSTANDING
# =========================
def extract_biomedical_entities(query):
    biomedical_keywords = [
        "atrial fibrillation", "diabetes", "oncology", "cancer",
        "cardiovascular", "wearable", "remote monitoring", "mobile health",
        "mhealth", "clinical trial", "patient outcomes", "quality of life",
        "patient-reported outcomes", "telemedicine", "digital health",
        "enrollment", "retention", "adverse events", "treatment",
        "monitoring", "ecg", "heart failure"
    ]

    found = []
    q = query.lower()

    for term in biomedical_keywords:
        if term in q:
            found.append(term)

    return found


def extract_pico(query):
    q = query.lower()

    pico = {
        "Population": "Not explicitly specified",
        "Intervention": "Not explicitly specified",
        "Comparison": "Not explicitly specified",
        "Outcome": "Not explicitly specified",
    }

    if any(x in q for x in ["patient", "patients", "adult", "clinical trial"]):
        pico["Population"] = "Patients / clinical study participants"

    if any(x in q for x in ["mobile health", "mhealth", "wearable", "remote monitoring", "telemedicine", "digital health"]):
        pico["Intervention"] = "Digital health / remote monitoring intervention"

    if any(x in q for x in ["usual care", "control", "compared", "comparison"]):
        pico["Comparison"] = "Usual care / comparator group"

    if any(x in q for x in ["outcome", "quality of life", "effectiveness", "retention", "enrollment", "barriers"]):
        pico["Outcome"] = "Patient outcomes / clinical effectiveness / study participation outcomes"

    return pico


def query_understanding_agent(query):
    entities = extract_biomedical_entities(query)
    pico = extract_pico(query)

    return {
        "original_query": query,
        "entities": entities,
        "pico": pico,
    }


# =========================
# AGENT STEP 2: QUERY REFORMULATION
# =========================
def query_reformulation_agent(query_analysis):
    query = query_analysis["original_query"]
    entities = query_analysis["entities"]

    combined_text = query + " " + " ".join(entities)

    words = combined_text.split()
    unique_words = list(dict.fromkeys(words))

    reformulated = " ".join(unique_words)
    reformulated = re.sub(r"\s+", " ", reformulated).strip()

    return reformulated


# =========================
# AGENT STEP 3: RETRIEVAL PLANNING
# =========================
def retrieval_planning_agent(query_analysis, user_top_k):
    return {
        "top_k": user_top_k,
        "strategy": "FAISS semantic retrieval with metadata-aware filtering",
    }


# =========================
# AGENT STEP 4: EVIDENCE RETRIEVAL
# =========================
def relevance_score(chunk, query):
    query_terms = get_terms(query)

    chunk_text = (
        str(chunk.get("title", "")) + " " +
        str(chunk.get("keywords", "")) + " " +
        str(chunk.get("section", "")) + " " +
        str(chunk.get("chunk_text", ""))
    )

    chunk_terms = get_terms(chunk_text)
    return len(query_terms.intersection(chunk_terms))


def retrieve_chunks(query, index, metadata, embed_model, top_k=3):
    query_embedding = embed_model.encode(
        [query],
        convert_to_numpy=True,
        normalize_embeddings=True
    ).astype("float32")

    search_k = min(max(top_k * 12, 30), index.ntotal)
    scores, indices = index.search(query_embedding, search_k)

    selected = []
    seen_chunk_ids = set()
    seen_pmcids = set()

    for score, idx in zip(scores[0], indices[0]):
        if idx < 0 or idx >= len(metadata):
            continue

        chunk = metadata[idx].copy()
        chunk["score"] = float(score)

        section = str(chunk.get("section", "")).lower()
        text = clean_display_text(chunk.get("chunk_text", ""))

        if section in {"references", "supplementary", "acknowledgments", "author_contributions", "title"}:
            continue

        if len(text.split()) < 60:
            continue

        score = relevance_score(chunk, query)

        query_words = set(get_terms(query))
        chunk_words = set(get_terms(chunk["chunk_text"]))

        overlap = len(query_words.intersection(chunk_words))

        important_terms = [
            word for word in query_words
            if len(word) > 4
        ]

        important_overlap = len(
            set(important_terms).intersection(chunk_words)
        )

        if score < 2:
            continue

        if overlap < 2:
            continue

        if important_overlap < 1:
            continue

        chunk_id = chunk.get("chunk_id", "")
        pmcid = chunk.get("pmcid", "")

        if chunk_id in seen_chunk_ids:
            continue

        if pmcid not in seen_pmcids:
            selected.append(chunk)
            seen_chunk_ids.add(chunk_id)
            seen_pmcids.add(pmcid)

        if len(selected) >= top_k:
            break

        # If filtering becomes too strict,
        # allow slightly relaxed retrieval
        # but still preserve query overlap

        if len(selected) < top_k:

            for score, idx in zip(scores[0], indices[0]):

                if idx < 0 or idx >= len(metadata):
                    continue

                chunk = metadata[idx].copy()
                chunk["score"] = float(score)

                chunk_id = chunk.get("chunk_id", "")
                pmcid = chunk.get("pmcid", "")

                if chunk_id in seen_chunk_ids:
                    continue

                if pmcid in seen_pmcids:
                    continue

                text = clean_display_text(
                    chunk.get("chunk_text", "")
                )

                if len(text.split()) < 60:
                    continue

                query_words = set(get_terms(query))
                chunk_words = set(get_terms(text))

                overlap = len(
                    query_words.intersection(chunk_words)
                )

                # relaxed fallback, but still requires query overlap
                if overlap < 1:
                    continue

                selected.append(chunk)
                seen_chunk_ids.add(chunk_id)
                seen_pmcids.add(pmcid)

                if len(selected) >= top_k:
                    break

    return selected[:top_k]


# =========================
# AGENT STEP 5: EVIDENCE SYNTHESIS
# =========================
def build_prompt(query, chunks, query_analysis):
    evidence_text = ""

    for i, chunk in enumerate(chunks, start=1):
        evidence_text += f"""
Evidence {i}:
Title: {chunk.get('title', '')}
PMCID: {chunk.get('pmcid', '')}
Section: {chunk.get('section', '')}
Text: {truncate_to_sentence(chunk.get('chunk_text', ''), 900)}
"""

    prompt = f"""
### Instruction:
You are an evidence-based biomedical research assistant.

Answer ONLY using the provided evidence.
Do not use external knowledge.
Do not hallucinate.
Generate the answer with exactly these sections:

Summary:
Key Findings:
Limitations:

For every key finding, include:
Source title | PMCID | Section

### Query Understanding:
Biomedical Entities: {query_analysis.get("entities", [])}
PICO: {query_analysis.get("pico", {})}

### Clinical Query:
{query}

### Retrieved Evidence:
{evidence_text}

### Response:
"""

    return prompt


def generate_answer(prompt, tokenizer, model, max_new_tokens=350):
    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True,
        max_length=4096
    ).to(model.device)

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            do_sample=False,
            repetition_penalty=1.25,
            no_repeat_ngram_size=3,
            pad_token_id=tokenizer.eos_token_id,
        )

    full_response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return full_response.replace(prompt, "").strip()


# =========================
# AGENT STEP 6: VALIDATION
# =========================
def validate_answer(answer):
    lower = answer.lower()

    has_summary = "summary" in lower
    has_key_findings = "key findings" in lower or "finding" in lower
    has_limitations = "limitations" in lower or "limitation" in lower
    has_pmcid = bool(re.search(r"pmc\d+", lower))

    bad_patterns = [
        "fetched:",
        "json document",
        "full response:",
        "clinicaldecision",
        "reportedoutcome",
        "thepatient",
        "```json",
    ]

    has_bad_pattern = any(p in lower for p in bad_patterns)

    score = 0
    score += 0.25 if has_summary else 0
    score += 0.25 if has_key_findings else 0
    score += 0.25 if has_limitations else 0
    score += 0.25 if has_pmcid else 0

    is_valid = score >= 0.75 and not has_bad_pattern

    return {
        "is_valid": is_valid,
        "structure_score": score,
        "has_summary": has_summary,
        "has_key_findings": has_key_findings,
        "has_limitations": has_limitations,
        "has_pmcid": has_pmcid,
        "has_bad_pattern": has_bad_pattern,
    }


def build_safe_evidence_answer(query, chunks):

    dynamic_summary = generate_dynamic_summary(chunks)

    answer = f"""Summary:
{dynamic_summary}

Key Findings:
"""

    for i, chunk in enumerate(chunks, start=1):

        evidence_preview = truncate_to_sentence(
            chunk.get("chunk_text", ""),
            320
        )

        answer += f"""
{i}. {evidence_preview}

   Source: {chunk.get('title', '')}
   PMCID: {chunk.get('pmcid', '')}
   Section: {chunk.get('section', '')}
"""

    answer += """

Limitations:
The answer is synthesized only from the retrieved biomedical evidence chunks. The retrieved excerpts may not represent the complete article or the entire biomedical literature. Clinical interpretation should be validated through full-paper review and expert assessment.
"""

    return answer


def calculate_confidence(chunks, validation_result):
    if not chunks:
        return 0.0

    avg_similarity = sum(chunk.get("score", 0) for chunk in chunks) / len(chunks)
    structure_score = validation_result.get("structure_score", 0)

    confidence = (0.7 * avg_similarity) + (0.3 * structure_score)
    return round(min(confidence, 1.0), 3)


# =========================
# STUDY COMPARISON TABLE
# =========================
def build_study_comparison_table(chunks):
    rows = []

    for i, chunk in enumerate(chunks, start=1):
        rows.append(
            {
                "Rank": i,
                "PMCID": chunk.get("pmcid", ""),
                "Title": chunk.get("title", ""),
                "Journal": chunk.get("journal", ""),
                "Year": chunk.get("year", ""),
                "Section": chunk.get("section", ""),
                "Similarity Score": round(chunk.get("score", 0), 4),
            }
        )

    return pd.DataFrame(rows)


# =========================
# RETRIEVAL EVALUATION
# =========================
TEST_QUERIES = [
    {
        "query": "atrial fibrillation mobile health patient outcomes",
        "expected_keywords": [
            "atrial fibrillation", "mobile health", "mhealth",
            "patient-reported", "outcomes", "quality of life", "telewear"
        ],
    },
    {
        "query": "oncology trial enrollment barriers",
        "expected_keywords": [
            "oncology", "cancer", "clinical trial", "enrollment", "barriers", "patients"
        ],
    },
    {
    "query": "remote patient monitoring clinical benefits",
    "expected_keywords": [
        "remote monitoring",
        "patient monitoring",
        "clinical benefits",
        "telemedicine",
        "digital health",
        "patient outcomes"
    ],
},
    {
        "query": "clinical trial patient retention strategies",
        "expected_keywords": [
            "clinical trial", "patient retention", "recruitment", "enrollment", "participation"
        ],
    },
    {
        "query": "wearable devices in cardiovascular monitoring",
        "expected_keywords": [
            "wearable", "cardiovascular", "ecg", "monitoring", "mobile health", "heart"
        ],
    },
]


def is_relevant(chunk, expected_keywords):
    combined_text = (
        str(chunk.get("title", "")) + " " +
        str(chunk.get("section", "")) + " " +
        str(chunk.get("keywords", "")) + " " +
        str(chunk.get("chunk_text", ""))
    ).lower()

    matched = [
        kw for kw in expected_keywords
        if kw.lower() in combined_text
    ]

    return len(matched) >= 1, matched


def dcg(relevances):
    score = 0.0

    for i, rel in enumerate(relevances, start=1):
        score += rel / math.log2(i + 1)

    return score


def ndcg_at_k(relevances):
    actual_dcg = dcg(relevances)
    ideal_dcg = dcg(sorted(relevances, reverse=True))

    if ideal_dcg == 0:
        return 0.0

    return actual_dcg / ideal_dcg


def run_retrieval_evaluation(index, metadata, embed_model, k):
    rows = []

    for test in TEST_QUERIES:
        query = test["query"]
        expected_keywords = test["expected_keywords"]

        chunks = retrieve_chunks(
            query=query,
            index=index,
            metadata=metadata,
            embed_model=embed_model,
            top_k=k,
        )

        relevances = []
        relevant_count = 0

        for rank, chunk in enumerate(chunks, start=1):
            relevant, matched = is_relevant(chunk, expected_keywords)
            rel_value = 1 if relevant else 0
            relevances.append(rel_value)

            if relevant:
                relevant_count += 1

            rows.append(
                {
                    "Query": query,
                    "Rank": rank,
                    "PMCID": chunk.get("pmcid", ""),
                    "Title": chunk.get("title", ""),
                    "Section": chunk.get("section", ""),
                    "Score": round(chunk.get("score", 0), 4),
                    "Relevant": relevant,
                    "Matched Keywords": ", ".join(matched),
                }
            )

        precision = relevant_count / max(k, 1)
        ndcg = ndcg_at_k(relevances)

        rows.append(
            {
                "Query": query,
                "Rank": "SUMMARY",
                "PMCID": "",
                "Title": "",
                "Section": "",
                "Score": "",
                "Relevant": f"Precision@{k}: {precision:.2f}",
                "Matched Keywords": f"NDCG@{k}: {ndcg:.2f}",
            }
        )

    return pd.DataFrame(rows)

def extract_text_from_uploaded_pdf(uploaded_file):
    pdf_bytes = uploaded_file.read()
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")

    text_parts = []

    for page_num, page in enumerate(doc, start=1):
        page_text = page.get_text("text")
        if page_text:
            text_parts.append(f"\n[Page {page_num}]\n{page_text}")

    text = "\n".join(text_parts)

    # remove excessive whitespace
    text = re.sub(r"\s+", " ", text)

    return clean_display_text(text)


def summarize_uploaded_pdf(pdf_text, tokenizer=None, model=None, max_new_tokens=250):
    if not pdf_text.strip():
        return "No readable text could be extracted from the uploaded PDF."

    text = clean_display_text(pdf_text)

    sentences = re.split(r'(?<=[.!?])\s+', text)

    useful_sentences = []
    keywords = [
        "objective", "background", "method", "methods", "result", "results",
        "conclusion", "case", "patient", "study", "finding", "treatment",
        "clinical", "outcome", "limitation"
    ]

    skip_patterns = [
    "received:",
    "accepted:",
    "revised:",
    "author(s)",
    "copyright",
]

    for sentence in sentences:
        sentence_clean = sentence.strip()

        if len(sentence_clean.split()) < 8:
            continue

        if len(sentence_clean) > 350:
            continue

        # Skip publication metadata
        if any(p in sentence_clean.lower() for p in skip_patterns):
            continue

        if any(k in sentence_clean.lower() for k in keywords):
            useful_sentences.append(sentence_clean)

    if len(useful_sentences) < 5:
        useful_sentences = [
            s.strip() for s in sentences
            if 8 <= len(s.strip().split()) <= 45
        ]

    selected = useful_sentences[1:7]

    summary = selected[0] if len(selected) > 0 else "The uploaded PDF text was extracted successfully, but a meaningful summary could not be generated from the available text."

    summary = re.sub(r"\s+", " ", summary).strip()
    summary = summary.replace("[Page 1]", "").strip()

    key_points = []

    for sentence in selected[2:6]:
        sub_sentences = re.split(r'(?<=[.!?])\s+', sentence)

        for sub in sub_sentences:
            sub = sub.strip()

            if len(sub.split()) >= 8:
                key_points.append(sub)

    key_points = key_points[:3]

    limitations = (
        "This summary is generated only from the extracted PDF text preview and may not cover the complete document. "
        "Full-paper review is recommended for clinical or research interpretation."
    )

    summary = re.sub(r"CASE BASED REVIEW", "", summary, flags=re.IGNORECASE)
    summary = re.sub(r"Received:.*?2020", "", summary)
    summary = re.sub(r"Abstract", "", summary, flags=re.IGNORECASE)
    summary = re.sub(r"\s+", " ", summary).strip()

    output = "Summary:\n"
    output += summary + "\n\n"

    output += "Key Points:\n"
    for point in key_points:
        output += f"\n• {point.strip()}\n"

    output += "\nLimitations:\n"
    output += f"- {limitations}"

    return output

# =========================
# STREAMLIT APP
# =========================
def main():
    st.title("🧬 Agentic Evidence-Based Clinical Research Assistant")
    st.caption(
        "Agentic RAG pipeline using PubMedBERT embeddings, FAISS retrieval, "
        "QLoRA-adapted BioMistral, response validation, and citation-grounded evidence display."
    )

    with st.sidebar:
        st.header("Settings")

        top_k = st.slider(
            "Number of retrieved evidence chunks",
            1,
            5,
            DEFAULT_TOP_K
        )

        max_new_tokens = st.slider(
            "Max answer tokens",
            100,
            600,
            350,
            step=50
        )

        st.markdown("---")

        st.markdown("""
        ### Agentic Workflow
        1. Query Understanding  
        2. PICO + Entity Extraction  
        3. Query Reformulation  
        4. Retrieval Planning  
        5. Evidence Retrieval  
        6. Evidence Synthesis  
        7. Response Validation  
        8. Final Evidence Output  
        """)

        st.markdown("---")
        st.write("### System Status")
        st.write(f"CUDA available: `{torch.cuda.is_available()}`")

        if torch.cuda.is_available():
            st.write(f"GPU: `{torch.cuda.get_device_name(0)}`")

    tab1, tab2, tab3 = st.tabs([
    "🧬 Research Agent",
    "📊 Retrieval Evaluation",
    "📄 PDF Summary"
    ])

    with tab1:
        query = st.text_area(
            "Enter your clinical research question:",
            value="atrial fibrillation mobile health patient outcomes",
            height=100,
        )

        st.markdown("""
        ### Example Queries
        - atrial fibrillation mobile health patient outcomes  
        - oncology trial enrollment barriers  
        - remote patient monitoring clinical benefits  
        - clinical trial patient retention strategies  
        - wearable devices in cardiovascular monitoring  
        """)

        run_button = st.button("Run Clinical Research Agent", type="primary")

        if run_button:
            if not query.strip():
                st.warning("Please enter a query.")
                return

            with st.spinner("Loading retrieval components and fine-tuned model..."):
                index, metadata, embed_model = load_retrieval_components()
                tokenizer, model = load_finetuned_model()

            with st.spinner("Agent Step 1: Understanding query..."):
                query_analysis = query_understanding_agent(query)

            with st.spinner("Agent Step 2: Reformulating query..."):
                reformulated_query = query_reformulation_agent(query_analysis)

            with st.spinner("Agent Step 3: Planning retrieval..."):
                retrieval_plan = retrieval_planning_agent(query_analysis, top_k)

            with st.spinner("Agent Step 4: Retrieving evidence..."):
                chunks = retrieve_chunks(
                    query=reformulated_query,
                    index=index,
                    metadata=metadata,
                    embed_model=embed_model,
                    top_k=retrieval_plan["top_k"],
                )

            if not chunks:
                st.error("No relevant evidence chunks found.")
                return

            with st.spinner("Agent Step 5: Synthesizing answer using QLoRA BioMistral..."):
                prompt = build_prompt(query, chunks, query_analysis)
                answer = generate_answer(
                    prompt=prompt,
                    tokenizer=tokenizer,
                    model=model,
                    max_new_tokens=max_new_tokens,
                )

            cleaned_answer = clean_display_text(answer)

            with st.spinner("Agent Step 6: Validating response..."):
                validation_result = validate_answer(cleaned_answer)

                if not validation_result["is_valid"]:
                    cleaned_answer = build_safe_evidence_answer(query, chunks)
                    validation_result = validate_answer(cleaned_answer)

                confidence = calculate_confidence(chunks, validation_result)

                try:
                    log_query_result(
                        query=query,
                        chunks=chunks,
                        confidence=confidence,
                        validation_score=validation_result["structure_score"],
                    )
                except Exception as e:
                    st.warning(f"Logging failed: {e}")

            st.success("Agentic evidence-based answer generated successfully.")

            col1, col2, col3 = st.columns(3)
            col1.metric("Confidence Score", confidence)
            col2.metric("Retrieved Evidence", len(chunks))
            col3.metric("Validation Score", validation_result["structure_score"])

            with st.expander("Agent Reasoning Trace", expanded=False):
                st.write("### Query Understanding")
                st.json(query_analysis)

                st.write("### Reformulated Query")
                st.write(reformulated_query)

                st.write("### Retrieval Plan")
                st.json(retrieval_plan)

                st.write("### Response Validation")
                st.json(validation_result)

            st.subheader("Generated Evidence-Based Answer")

            formatted_answer = cleaned_answer.replace(
                "Summary:", "### Summary\n"
            ).replace(
                "Key Findings:", "\n### Key Findings\n"
            ).replace(
                "Limitations:", "\n### Limitations\n"
            )

            st.markdown(formatted_answer)

            st.subheader("Study Comparison Table")
            comparison_df = build_study_comparison_table(chunks)
            st.dataframe(comparison_df, use_container_width=True)

            st.subheader("Retrieved Evidence Sources")

            for i, chunk in enumerate(chunks, start=1):
                with st.expander(
                    f"Evidence {i}: {chunk.get('title', '')} | {chunk.get('pmcid', '')} | {chunk.get('section', '')}"
                ):
                    st.write(f"**Similarity Score:** {chunk.get('score', 0):.4f}")
                    st.write(f"**Title:** {chunk.get('title', '')}")
                    st.write(f"**PMCID:** {chunk.get('pmcid', '')}")
                    st.write(f"**Journal:** {chunk.get('journal', '')}")
                    st.write(f"**Year:** {chunk.get('year', '')}")
                    st.write(f"**Section:** {chunk.get('section', '')}")
                    st.write("**Evidence Preview:**")
                    st.write(truncate_to_sentence(chunk.get("chunk_text", ""), 900))

    with tab2:
        st.subheader("Retrieval Evaluation")

        st.write(
            "This evaluates the retrieval layer using representative biomedical queries "
            "with Precision@K and NDCG@K."
        )
        
        eval_k = st.selectbox("Select K", [3, 5], index=0)

        if st.button("Run Retrieval Evaluation"):
            with st.spinner("Running retrieval evaluation..."):
                index, metadata, embed_model = load_retrieval_components()
                eval_df = run_retrieval_evaluation(
                    index=index,
                    metadata=metadata,
                    embed_model=embed_model,
                    k=eval_k,
                )

            st.dataframe(eval_df, use_container_width=True)

            csv_data = eval_df.to_csv(index=False).encode("utf-8-sig")
            st.download_button(
                label="Download Retrieval Evaluation CSV",
                data=csv_data,
                file_name=f"retrieval_evaluation_k{eval_k}.csv",
                mime="text/csv",
            )

    with tab3:
        st.subheader("Uploaded PDF Summarization")

        st.write(
            "Upload a biomedical PDF to generate a lightweight summary from the uploaded document. "
            "This feature summarizes the uploaded PDF text directly and does not modify the existing FAISS vector database."
        )

        uploaded_pdf = st.file_uploader(
            "Upload biomedical PDF",
            type=["pdf"]
        )

        if uploaded_pdf is not None:
            st.success(f"Uploaded file: {uploaded_pdf.name}")

            with st.spinner("Extracting text from uploaded PDF..."):
                uploaded_text = extract_text_from_uploaded_pdf(uploaded_pdf)

            st.write("Extracted text length:", len(uploaded_text), "characters")

            with st.expander("Preview extracted text"):
                st.write(uploaded_text[:1500])

            if st.button("Generate PDF Summary"):
                with st.spinner("Generating extractive PDF summary..."):
                    pdf_summary = summarize_uploaded_pdf(
                        pdf_text=uploaded_text
                    )

                pdf_summary = pdf_summary.strip()

                formatted_summary = pdf_summary.replace(
                    "Summary:", "### Summary\n"
                ).replace(
                    "Key Points:", "\n### Key Points\n"
                ).replace(
                    "Limitations:", "\n### Limitations\n"
                )

                st.subheader("Generated PDF Summary")
                st.markdown(formatted_summary)

if __name__ == "__main__":
    main()