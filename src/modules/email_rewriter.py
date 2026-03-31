"""
Email Rewriter Module
Transforms casual or poorly worded text into professional business emails.
"""

from src.utils.llm_utils import build_chain

EMAIL_PROMPT = """
You are a professional business communication specialist.

Rewrite the following informal or unstructured message as a polished, professional business email.

Original Message: {message}
Recipient Type: {recipient_type}
Tone: {tone}

Requirements:
- Include a proper Subject line
- Use formal greeting and closing
- Keep it concise and action-oriented
- Maintain the core intent of the original message
- Match the tone ({tone})

Output Format:
Subject: ...

Dear [Recipient],

[Body]

Best regards,
[Your Name]
"""

def rewrite_email(message: str, recipient_type: str = "Manager", tone: str = "Formal") -> str:
    chain = build_chain(EMAIL_PROMPT, ["message", "recipient_type", "tone"], temperature=0.5)
    return chain.invoke({"message": message, "recipient_type": recipient_type, "tone": tone})
