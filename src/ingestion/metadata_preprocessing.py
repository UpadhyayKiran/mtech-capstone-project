import os
import re
import json
from cv2 import line
import pandas as pd
import pymupdf as fitz  # PyMuPDF
from pathlib import Path


# =========================
# CONFIG
# =========================
PDF_FOLDER = r"data\raw_pdfs"
METADATA_CSV = r"data\metadata\metadata_pdf_152_cleaned.csv"
OUTPUT_FOLDER = r"data\json"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)


# =========================
# LOAD METADATA
# =========================
def load_metadata(csv_path):
    df = pd.read_csv(csv_path)

    # normalize column names
    df.columns = [col.strip().lower() for col in df.columns]

    # expected pmcid column
    if "pmcid" not in df.columns:
        raise ValueError("Metadata CSV must contain a 'pmcid' column.")

    df["pmcid"] = df["pmcid"].astype(str).str.strip()

    # fill NaN safely
    df = df.fillna("")

    metadata_map = {}
    for _, row in df.iterrows():
        pmcid = row["pmcid"]
        metadata_map[pmcid] = row.to_dict()

    return metadata_map


# =========================
# PDF TEXT EXTRACTION
# =========================
def extract_text_from_pdf(pdf_path):
    text_blocks = []

    try:
        doc = fitz.open(pdf_path)
        for page in doc:
            page_text = page.get_text("text")
            if page_text:
                text_blocks.append(page_text)
        doc.close()
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
        return ""

    return "\n".join(text_blocks)


# =========================
# BASIC CLEANING
# =========================
def normalize_text(text):
    if not text:
        return ""

    # normalize line endings
    text = text.replace("\r", "\n")

    # fix ligatures / odd unicode
    replacements = {
        "\ufb01": "fi",
        "\ufb02": "fl",
        "\u2013": "-",
        "\u2014": "-",
        "\u2018": "'",
        "\u2019": "'",
        "\u201c": '"',
        "\u201d": '"',
        "\xa0": " ",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)

    # remove repeated noisy OCR/artifact lines like a1111111111
    text = re.sub(r"\b[aA]1{5,}\b", " ", text)

    # remove page numbers standing alone
    text = re.sub(r"(?m)^\s*\d+\s*$", " ", text)

    # remove excessive blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)

    # collapse excessive spaces
    text = re.sub(r"[ \t]{2,}", " ", text)

    return text.strip()


# =========================
# HEADER / FOOTER REDUCTION
# =========================
def remove_repeated_noise(text):
    lines = text.splitlines()
    cleaned_lines = []

    for line in lines:
        stripped = line.strip()
        lower = stripped.lower()

        if not stripped:
            continue

        # REMOVE running headers / footers
        if re.search(r"plos one|doi\.org|/\s*\d+\s*$", lower):
            continue

        if re.search(r"costs of ct with anticancer", lower):
            continue

        # REMOVE page numbers like "1 / 12"
        if re.match(r"^\d+\s*/\s*\d+$", stripped):
            continue

        # REMOVE standalone years/pages
        if re.match(r"^\d{4}\s*$", stripped):
            continue

        # REMOVE dates like "January 8, 2019"
        if re.search(
            r"\b(january|february|march|april|may|june|july|august|september|october|november|december)\b.*\d{4}",
            lower,
        ):
            continue
        cleaned_lines.append(stripped)

    return "\n".join(cleaned_lines)


# =========================
# TITLE EXTRACTION
# =========================
def infer_title(text, fallback_title=""):
    """
    Tries to infer title from top of first page text.
    Falls back to metadata title if available.
    """
    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]

    if fallback_title:
        return fallback_title.strip()

    title_candidates = []
    for line in lines[:20]:
        # ignore generic journal/front matter labels
        if line.lower() in {"research article", "open access", "abstract"}:
            continue
        if len(line.split()) >= 4 and not re.search(
            r"@|doi\.org|received:|accepted:|published:", line.lower()
        ):
            title_candidates.append(line)

    if title_candidates:
        return max(title_candidates, key=len).strip()

    return ""


# =========================
# AUTHOR EXTRACTION
# =========================
def clean_author_name(name):
    name = re.sub(r"\b\d+\b", "", name)
    name = re.sub(r"\bID\b", "", name, flags=re.IGNORECASE)
    name = re.sub(r"[*†‡§¶#]+", "", name)
    name = re.sub(r"\s{2,}", " ", name)
    return name.strip(" ,;-")


def extract_authors_from_text(text):
    """
    Very light extraction from author-like lines near top.
    Metadata authors should still be preferred if present.
    """
    first_chunk = "\n".join(text.splitlines()[:80])

    email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
    first_chunk = re.sub(email_pattern, " ", first_chunk)

    # Try to capture author block before abstract/introduction
    stop_words = ["abstract", "introduction", "aim", "background", "methods"]
    lines = [ln.strip() for ln in first_chunk.splitlines() if ln.strip()]

    candidate_lines = []
    for line in lines:
        if line.lower() in stop_words:
            break
        candidate_lines.append(line)

    block = " ".join(candidate_lines)

    # split by commas if it looks author-like
    raw_parts = re.split(r",", block)
    authors = []

    for part in raw_parts:
        part = clean_author_name(part)
        # keep human-like names only
        if 2 <= len(part.split()) <= 5 and re.match(
            r"^[A-Za-zÀ-ÖØ-öø-ÿ'`\-.\s]+$", part
        ):
            if not re.search(
                r"\b(university|department|institute|hospital|napoli|italy|unit)\b",
                part,
                re.I,
            ):
                authors.append(part)

    # deduplicate while preserving order
    unique_authors = []
    seen = set()
    for a in authors:
        key = a.lower()
        if a and key not in seen:
            seen.add(key)
            unique_authors.append(a)

    return unique_authors


# =========================
# ABSTRACT EXTRACTION
# =========================
def extract_abstract(text):
    text_lower = text.lower()

    # Try normal abstract
    match = re.search(
        r"\babstract\b(.*?)(\bintroduction\b|\bbackground\b)",
        text,
        flags=re.IGNORECASE | re.DOTALL,
    )
    if match:
        return cleanup_section_text(match.group(1))

    # Structured abstract (Aim/Methods/Results/Conclusion)
    pattern = re.search(
        r"(aim.*?)(introduction)", text, flags=re.IGNORECASE | re.DOTALL
    )

    if pattern:
        return cleanup_section_text(pattern.group(1))

    return ""


# =========================
# SECTION SPLITTING
# =========================
SECTION_PATTERNS = {
    "abstract": [
        r"^\s*abstract\s*$",
    ],
    "introduction": [
        r"^\s*introduction\s*$",
        r"^\s*background\s*$",
    ],
    "methods": [
        r"^\s*methods\s*$",
        r"^\s*materials and methods\s*$",
        r"^\s*methodology\s*$",
        r"^\s*patients and methods\s*$",
    ],
    "results": [
        r"^\s*results\s*$",
    ],
    "discussion": [
        r"^\s*discussion\s*$",
    ],
    "conclusion": [
        r"^\s*conclusion[s]?\s*$",
        r"^\s*concluding remarks\s*$",
    ],
    "acknowledgments": [
        r"^\s*acknowledg?ments?\s*$",
    ],
    "references": [
        r"^\s*references\s*$",
        r"^\s*bibliography\s*$",
    ],
    "supplementary": [
        r"^\s*supporting information\s*$",
        r"^\s*supplementary information\s*$",
    ],
    "author_contributions": [
        r"^\s*author contributions\s*$",
    ],
}


def identify_heading(line):
    stripped = line.strip()

    for section, patterns in SECTION_PATTERNS.items():
        for pattern in patterns:
            if re.match(pattern, stripped, flags=re.IGNORECASE):
                return section

    return None


def split_into_sections(text):
    lines = text.splitlines()

    sections = []
    current_section = "unknown"
    buffer = []

    for line in lines:
        detected = identify_heading(line)

        if detected:
            # store previous
            section_text = "\n".join(buffer).strip()
            if section_text:
                sections.append(
                    {
                        "section": current_section,
                        "text": cleanup_section_text(section_text),
                    }
                )
            current_section = detected
            buffer = []
        else:
            buffer.append(line)

    # last section
    section_text = "\n".join(buffer).strip()
    if section_text:
        sections.append(
            {"section": current_section, "text": cleanup_section_text(section_text)}
        )

    # remove empty
    sections = [s for s in sections if s["text"].strip()]

    return sections


# =========================
# SECTION TEXT CLEANUP
# =========================
def cleanup_section_text(text):
    if not text:
        return ""

    # remove author contribution / publisher junk inside scientific sections
    junk_patterns = [
        r"open access",
        r"citation:",
        r"editor:",
        r"received:",
        r"accepted:",
        r"published:",
        r"copyright:",
        r"data availability statement:",
        r"funding:",
        r"competing interests:",
    ]

    lines = text.splitlines()
    cleaned = []

    for line in lines:
        lower = line.strip().lower()

        if any(lower.startswith(p) for p in junk_patterns):
            continue

        # remove DOI figure/table URLs only if they are isolated URLs
        if re.match(r"^https?://doi\.org/", lower):
            continue

        # REMOVE figure/table captions
        if re.match(r"^(fig|table)\s*\d+", lower):
            continue
        cleaned.append(line)

    text = "\n".join(cleaned)

    # fix hyphenation across line breaks: anti-\ncancer -> anticancer
    text = re.sub(r"(\w)-\n(\w)", r"\1\2", text)

    # join lines carefully, but preserve paragraph gaps
    text = re.sub(r"(?<!\n)\n(?!\n)", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)

    # collapse spaces
    text = re.sub(r"[ \t]{2,}", " ", text)

    return text.strip()


# =========================
# FRONT MATTER SEPARATION
# =========================
def extract_front_matter(text):
    """
    Extract content before abstract/introduction.
    Useful for title/authors/affiliations.
    """
    lower = text.lower()

    stops = []
    for marker in [
        "abstract",
        "introduction",
        "background",
        "aim",
        "methods",
        "materials and methods",
    ]:
        idx = lower.find(marker)
        if idx != -1:
            stops.append(idx)

    if not stops:
        return text[:3000]

    cut = min(stops)
    return text[:cut].strip()


def extract_affiliations(front_matter):
    lines = [ln.strip() for ln in front_matter.splitlines() if ln.strip()]

    affiliations = []
    for line in lines:
        if len(line.split()) < 5:
            continue

        if re.search(
            r"\b(university|department|institute|hospital|centre|center|unit|college|school|italy|india)\b",
            line,
            re.I,
        ):
            # REMOVE title leakage
            if len(line) > 200:
                continue

        # REMOVE title leakage (IMPORTANT)
        if line.lower().startswith("costs of"):
            continue

        if "activity-based costing" in line.lower() and len(line.split()) < 12:
            continue

        affiliations.append(line)

    return list(dict.fromkeys(affiliations))


# =========================
# POST-PROCESS SECTION LABELS
# =========================
def refine_sections(sections, full_text, title):
    refined = []

    front_matter = extract_front_matter(full_text)

    # Add title/front matter explicitly if useful
    if title:
        refined.append({"section": "title", "text": title})

    affiliations = extract_affiliations(front_matter)
    if affiliations:
        refined.append({"section": "affiliations", "text": " ".join(affiliations)})

    found_abstract = False

    for sec in sections:
        sec_name = sec["section"]
        sec_text = sec["text"].strip()

        if not sec_text:
            continue

        # skip duplicated title in unknown
        if sec_name == "unknown" and title and sec_text.startswith(title[:40]):
            continue

        # skip author-only/front-matter pollution in methods
        if sec_name == "methods":
            if re.search(r"@|university|department|institute|hospital", sec_text, re.I):
                if len(sec_text.split()) < 300:
                    continue

        if sec_name == "abstract":
            found_abstract = True

        refined.append({"section": sec_name, "text": sec_text})

    # fallback abstract if not properly extracted
    if not found_abstract:
        abs_text = extract_abstract(full_text)
        if abs_text:
            refined.insert(1, {"section": "abstract", "text": abs_text})

    return refined


# =========================
# MAIN PROCESSING
# =========================
def build_output_record(pmcid, pdf_filename, pdf_path, raw_text, metadata):
    raw_text = normalize_text(raw_text)
    raw_text = remove_repeated_noise(raw_text)

    title = infer_title(raw_text, metadata.get("title", ""))
    front_matter = extract_front_matter(raw_text)

    # Prefer metadata authors if available
    authors = []
    if "authors" in metadata and str(metadata["authors"]).strip():
        possible = str(metadata["authors"]).strip()

        # if metadata authors already stored as string list
        if possible.startswith("[") and possible.endswith("]"):
            try:
                parsed = json.loads(possible)
                if isinstance(parsed, list):
                    authors = [str(a).strip() for a in parsed if str(a).strip()]
            except Exception:
                authors = []
        else:
            split_authors = [a.strip() for a in re.split(r";|,", possible) if a.strip()]
            authors = split_authors

    if not authors:
        authors = extract_authors_from_text(front_matter)

    abstract = metadata.get("abstract", "").strip()
    if not abstract:
        abstract = extract_abstract(raw_text)

    # create sections
    sections = split_into_sections(raw_text)
    sections = refine_sections(sections, raw_text, title)

    record = {
        "pmcid": pmcid,
        "source": pdf_filename,
        "pdf_path": pdf_path,
        "title": title,
        "year": str(metadata.get("year", "")).strip(),
        "journal": str(metadata.get("journal", "")).strip(),
        "authors": authors,
        "abstract": abstract,
        "keywords": str(metadata.get("keywords", "")).strip(),
        "sections": sections,
    }

    return record


def process_all_pdfs(pdf_folder, metadata_map, output_folder):
    pdf_files = [f for f in os.listdir(pdf_folder) if f.lower().endswith(".pdf")]

    if not pdf_files:
        print("No PDF files found.")
        return

    for idx, pdf_file in enumerate(pdf_files, start=1):
        pdf_path = os.path.join(pdf_folder, pdf_file)
        pmcid = Path(pdf_file).stem.strip()

        print(f"[{idx}/{len(pdf_files)}] Processing {pdf_file} ...")

        raw_text = extract_text_from_pdf(pdf_path)
        if not raw_text.strip():
            print(f"Skipping {pdf_file} because no text was extracted.")
            continue

        metadata = metadata_map.get(pmcid, {})

        record = build_output_record(
            pmcid=pmcid,
            pdf_filename=pdf_file,
            pdf_path=pdf_path,
            raw_text=raw_text,
            metadata=metadata,
        )

        output_path = os.path.join(output_folder, f"{pmcid}.json")
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(record, f, indent=2, ensure_ascii=False)

    print("\nProcessing complete.")


# =========================
# ENTRY POINT
# =========================
if __name__ == "__main__":
    metadata_map = load_metadata(METADATA_CSV)
    process_all_pdfs(PDF_FOLDER, metadata_map, OUTPUT_FOLDER)
