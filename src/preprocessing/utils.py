import os
import json
from langchain_core.documents import Document

def load_json_documents(input_dir):
    documents = []

    for file in os.listdir(input_dir):
        if file.endswith(".json"):
            with open(os.path.join(input_dir, file), "r", encoding="utf-8") as f:
                data = json.load(f)

                pmcid = data["pmcid"]
                title = data["title"]
                source = data["source"]
                pdf_path = data["pdf_path"]
                journal = data["journal"]
                year = data["year"]
                authors = ", ".join(data["authors"])
                abstract = data["abstract"]
                sections = data["sections"]

    
                documents.append(
                   Document(
                       page_content = abstract,
                       metadata = {
                           "pmcid": pmcid,
                           "title": title,
                           "source": source,
                           "pdf_path": pdf_path,
                           "journal": journal,
                           "year": year,
                           "authors": authors,
                           "section": "abstract"
                           }
                       )
                   )
    
                    # Sections
                for sec in sections:
                        documents.append(
                            Document(
                                page_content=sec["text"],
                                metadata = {
                                    "pmcid": pmcid,
                                    "title": title,
                                    "source": source,
                                    "pdf_path": pdf_path,
                                    "journal": journal,
                                    "year": year,
                                    "authors": authors,
                                    "section": sec["section"],
                                }
                            )
                        )
                  
    return documents
✅
