"""
Information Extractor Module
Extracts structured key entities from unstructured workplace text.
"""

from src.utils.llm_utils import build_chain

EXTRACTOR_PROMPT = """
You are a professional information extraction engine for workplace documents.

Extract the following entities from the given text and return them in a clean structured format:
- Person Name(s)
- Date(s) / Time(s)
- Task / Action Item
- Project / Department (if mentioned)
- Priority (High/Medium/Low — infer from context)
- Deadline (if mentioned)

Text: {text}

If a field is not found, write "Not mentioned".

Return the output as:
Person Name: ...
Date/Time: ...
Task/Action Item: ...
Project/Department: ...
Priority: ...
Deadline: ...
"""

def extract_info(text: str) -> str:
    chain = build_chain(EXTRACTOR_PROMPT, ["text"], temperature=0.1)
    return chain.invoke({"text": text})
