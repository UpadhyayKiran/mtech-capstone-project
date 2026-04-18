import pandas as pd
import shutil
import os

# ==== PATHS ====
CSV_FILE = "final_pdf_metadata_152_records_balanced.csv"
SOURCE_FOLDER = "pdfs"
DEST_FOLDER = "selected_152_pdfs"

# Create destination folder if not exists
os.makedirs(DEST_FOLDER, exist_ok=True)

# Load CSV
df = pd.read_csv(CSV_FILE)

# Get PMCIDs
pmcids = df["pmcid"].astype(str).str.strip().tolist()

copied = 0
missing = 0

for pmcid in pmcids:
    filename = f"{pmcid}.pdf"
    src_path = os.path.join(SOURCE_FOLDER, filename)
    dest_path = os.path.join(DEST_FOLDER, filename)

    if os.path.exists(src_path):
        shutil.copy2(src_path, dest_path)
        copied += 1
    else:
        print(f"Missing: {filename}")
        missing += 1

print("\n==== Summary ====")
print(f"Total expected: {len(pmcids)}")
print(f"Copied: {copied}")
print(f"Missing: {missing}")
print(f"Saved to: {DEST_FOLDER}")