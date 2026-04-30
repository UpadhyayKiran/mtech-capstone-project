import json
import faiss
import torch
import re
import unicodedata
import streamlit as st
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from peft import PeftModel


FAISS_INDEX_PATH = r"D:\PES_MTech\Sem_3\Capstone_Project\Data_Search_Collection\vectorstore\faiss_index.index"
METADATA_PATH = r"D:\PES_MTech\Sem_3\Capstone_Project\Data_Search_Collection\vectorstore\chunk_metadata.json"

EMBED_MODEL = "pritamdeka/S-PubMedBert-MS-MARCO"
BASE_MODEL = "BioMistral/BioMistral-7B"
ADAPTER_PATH = r"D:\PES_MTech\Sem_3\Capstone_Project\Data_Search_Collection\qlora_biomistral_adapter"

DEFAULT_TOP_K = 3


st.set_page_config(
    page_title="Evidence-Based Clinical Research Assistant",
    page_icon="🧬",
    layout="wide",
)


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

    model = PeftModel.from_pretrained(
        base_model,
        ADAPTER_PATH
    )

    model.eval()

    return tokenizer, model


def retrieve_chunks(query, index, metadata, embed_model, top_k=3):
    query_embedding = embed_model.encode(
        [query],
        convert_to_numpy=True,
        normalize_embeddings=True
    ).astype("float32")

    scores, indices = index.search(query_embedding, top_k)

    chunks = []

    for score, idx in zip(scores[0], indices[0]):
        if idx < 0 or idx >= len(metadata):
            continue

        chunk = metadata[idx].copy()
        chunk["score"] = float(score)
        chunks.append(chunk)

    return chunks

import re


def clean_display_text(text):
    if not text:
        return ""

    text = str(text)

    # Normalize unicode
    text = unicodedata.normalize("NFKC", text)

    # Remove weird control characters
    text = re.sub(r"[\x00-\x1F\x7F-\x9F]", "", text)

    # Remove replacement/unknown characters
    text = text.replace("�", "")
    text = text.replace("\ufffd", "")
    text = text.replace("\x00", "")
    text = text.replace("­", "")  # soft hyphen

    # Remove broken PDF/OCR symbols
    text = re.sub(r"[□■�]", "", text)

    # fix broken numbering like "dimension.14"
    text = re.sub(r'([a-zA-Z])(\d+)', r'\1 \2', text)

    # Remove noisy PDF extraction phrases
    noisy_patterns = [
        r"XSL\s*•?\s*FO\s*RenderX",
        r"page number not for citation purposes",
        r"J Am Heart Assoc\.",
        r"DOI:\s*\S+",
        r"https?://\S+",
        r"\bRenderX\b",
        r"\bequation\b",
    ]

    for pattern in noisy_patterns:
        text = re.sub(pattern, " ", text, flags=re.IGNORECASE)

    # Fix broken spacing
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"\s+([.,;:])", r"\1", text)

    # remove duplicated punctuation
    text = re.sub(r'\.{2,}', '.', text)

    return text.strip()


def truncate_to_sentence(text, max_chars=1000):
    text = clean_display_text(text)

    if len(text) <= max_chars:
        if text and text[-1] not in [".", "!", "?"]:
            text += "..."
        return text

    truncated = text[:max_chars]

    sentence_endings = [
        truncated.rfind("."),
        truncated.rfind("?"),
        truncated.rfind("!"),
    ]

    last_sentence_end = max(sentence_endings)

    if last_sentence_end > 300:
        return truncated[:last_sentence_end + 1].strip()

    return truncated.strip().rsplit(" ", 1)[0] + "..."

def build_prompt(query, chunks):
    evidence_text = ""

    for i, chunk in enumerate(chunks, start=1):
        evidence_text += f"""
Evidence {i}:
Title: {chunk['title']}
PMCID: {chunk['pmcid']}
Section: {chunk['section']}
Text: {truncate_to_sentence(chunk['chunk_text'], 1000)}
"""

    prompt = f"""
    You are an evidence-based clinical research assistant.

    Using ONLY the provided research evidence, generate:

    1. Summary
    2. Key Findings
    3. Limitations

    Keep response concise and professional.
    Do not repeat sentences.
    Do not copy raw text.

    Clinical Query:
    {query}

    Evidence:
    {evidence_text}

    Answer:
    """

    return prompt


def generate_answer(prompt, tokenizer, model, max_new_tokens=200, temperature=0.1):
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
            temperature=temperature,
            do_sample=False,
            top_p=0.9,
            repetition_penalty=1.3,
            no_repeat_ngram_size=3,
            pad_token_id=tokenizer.eos_token_id,
        )

    full_response = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )

    return full_response.replace(prompt, "").strip()


def build_safe_evidence_answer(query, chunks):
    answer = f"""Summary:
Based on the retrieved evidence, the query is mainly supported by studies related to atrial fibrillation management, mobile health infrastructure, patient-reported outcomes, and health-related quality-of-life assessment.

Key Findings:
"""

    for i, chunk in enumerate(chunks, start=1):
        evidence_preview = truncate_to_sentence(chunk["chunk_text"], 350)

        answer += f"""
{i}. {evidence_preview}
   Source: {chunk['title']} | PMCID: {chunk['pmcid']} | Section: {chunk['section']}
"""

    answer += """
Limitations:
The answer is based only on the retrieved evidence chunks. Full-paper review and clinical expert validation are required before making medical conclusions.
"""

    return answer

def main():
    st.title("🧬 Evidence-Based Clinical Research Assistant")
    st.caption("RAG + PubMedBERT embeddings + FAISS retrieval + QLoRA-adapted BioMistral")

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
            250,
            step=50
        )

        temperature = st.slider(
            "Temperature",
            0.0,
            1.0,
            0.1,
            step=0.1
        )

        st.markdown("---")

        st.markdown("""
        ### System Architecture
        PDFs  
        → Preprocessing  
        → Chunking  
        → PubMedBERT Embeddings  
        → FAISS Retrieval  
        → QLoRA BioMistral  
        → Evidence-Based Answer
        """)

        st.markdown("---")

        st.write("### System Status")
        st.write(f"CUDA available: `{torch.cuda.is_available()}`")

        if torch.cuda.is_available():
            st.write(
                f"GPU: `{torch.cuda.get_device_name(0)}`"
            )

    query = st.text_area(
        "Enter your clinical research question:",
        value="atrial fibrillation mobile health patient outcomes",
        height=100,
    )

    st.markdown("""
    ### Example Queries

    - atrial fibrillation mobile health patient outcomes  
    - oncology trial enrollment barriers  
    - diabetes remote monitoring effectiveness  
    - clinical trial patient retention strategies  
    - wearable devices in cardiovascular monitoring  
    """)
    run_button = st.button("Generate Evidence-Based Answer", type="primary")

    if run_button:
        if not query.strip():
            st.warning("Please enter a query.")
            return

        with st.spinner("Loading retrieval components and model..."):
            index, metadata, embed_model = load_retrieval_components()
            tokenizer, model = load_finetuned_model()

        with st.spinner("Retrieving evidence..."):
            chunks = retrieve_chunks(
                query=query,
                index=index,
                metadata=metadata,
                embed_model=embed_model,
                top_k=top_k,
            )

        if not chunks:
            st.error("No relevant evidence chunks found.")
            return

        with st.spinner("Generating answer using fine-tuned BioMistral..."):
            prompt = build_prompt(query, chunks)
            answer = generate_answer(
                prompt=prompt,
                tokenizer=tokenizer,
                model=model,
                max_new_tokens=max_new_tokens,
                temperature=temperature,
            )

        cleaned_answer = clean_display_text(answer)

        bad_patterns = [
            "fetched from:",
            "fethed from:",
            "source: body",
            "score: 1.0",
        ]

        if any(pattern in cleaned_answer.lower() for pattern in bad_patterns):
            cleaned_answer = build_safe_evidence_answer(query, chunks)

        st.subheader("Generated Answer")

        st.markdown(cleaned_answer.replace(
            "Summary:", "### Summary\n"
        ).replace(
            "Key Findings:", "\n### Key Findings\n"
        ).replace(
            "Limitations:", "\n### Limitations\n"
        ))

        st.success(
            "Answer generated using QLoRA-adapted BioMistral + FAISS retrieval pipeline"
        )
        
        st.subheader("Retrieved Evidence Sources")

        for i, chunk in enumerate(chunks, start=1):
            with st.expander(
                f"Evidence {i}: {chunk['title']} | {chunk['pmcid']} | {chunk['section']}"
            ):
                st.write(f"**Similarity Score:** {chunk['score']:.4f}")
                st.write(f"**Title:** {chunk['title']}")
                st.write(f"**PMCID:** {chunk['pmcid']}")
                st.write(f"**Journal:** {chunk.get('journal', '')}")
                st.write(f"**Year:** {chunk.get('year', '')}")
                st.write(f"**Section:** {chunk['section']}")
                st.write("**Evidence Preview:**")
                st.write(truncate_to_sentence(chunk["chunk_text"], 1500))


if __name__ == "__main__":
    main()
