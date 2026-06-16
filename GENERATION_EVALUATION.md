# Generation Evaluation Summary

The generation module was evaluated using automated checks for:

- response structure
- grounding overlap
- limitations section
- PMCID/source traceability
- answer length

Current observed generation quality improved after QLoRA training and prompt restructuring.

The system also includes runtime validation checks in the Streamlit UI:
- Summary present
- Key Findings present
- Limitations present
- PMCID present
- bad output pattern detection