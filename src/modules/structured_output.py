"""
Structured Output Generator Module
Converts free-form text into structured JSON for analytics and automation.
"""

from src.utils.llm_utils import build_chain

STRUCTURED_PROMPT = """
You are a data extraction and structuring specialist.

Convert the following workplace text into a clean, valid JSON object.

Text: {text}
Document Type: {doc_type}

Extract all relevant fields based on the document type and return ONLY a valid JSON object.
No explanation, no markdown, just the raw JSON.

For a meeting note: extract attendees, date, agenda, decisions, action_items, next_meeting
For an incident report: extract reporter, date, incident_type, description, severity, resolution
For a task description: extract task_name, assignee, due_date, priority, description, dependencies
For general text: extract any meaningful key-value pairs

Return only the JSON object.
"""

def generate_structured_output(text: str, doc_type: str = "general text") -> str:
    chain = build_chain(STRUCTURED_PROMPT, ["text", "doc_type"], temperature=0.1)
    return chain.invoke({"text": text, "doc_type": doc_type})
