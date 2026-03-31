"""
Ticket Classifier Module
Classifies support tickets into HR, Technical, Finance, or General categories.
"""

from src.utils.llm_utils import build_chain

TICKET_PROMPT = """
You are an intelligent IT support ticket classifier for a professional organization.

Your task is to classify the following support ticket into exactly ONE of these categories:
- HR: Related to human resources, leave, payroll, onboarding, policies, employee benefits
- Technical: Related to software, hardware, IT infrastructure, bugs, access issues
- Finance: Related to expenses, invoices, reimbursements, budget, accounting
- General: Any other workplace queries not fitting the above

Ticket: {ticket}

Respond in this exact format:
Category: <CATEGORY>
Confidence: <High/Medium/Low>
Reason: <One sentence explanation>
Suggested Action: <What team should handle this and how>
"""

def classify_ticket(ticket_text: str) -> str:
    chain = build_chain(TICKET_PROMPT, ["ticket"], temperature=0.1)
    return chain.invoke({"ticket": ticket_text})
