"""
Multi-Step Chain Module
Core LangChain LCEL showcase: classifies an issue AND generates a professional response.
"""

from src.utils.llm_utils import build_chain, get_llm
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

CLASSIFY_PROMPT = """
You are an intelligent workplace issue classifier.

Classify this employee issue and provide context for the response team.

Issue: {issue}

Output:
Category: <HR / Technical / Finance / General>
Urgency: <Critical / High / Medium / Low>
Summary: <One sentence summary>
"""

RESPONSE_PROMPT = """
You are a professional workplace support representative.

Based on the classification below, write a helpful, empathetic, and actionable response to the employee.

Classification:
{classification}

Original Issue:
{issue}

Write a professional response that:
1. Acknowledges the employee's concern
2. Provides clear next steps
3. Sets realistic expectations
4. Ends with encouragement

Response:
"""

def run_multi_step_chain(issue: str) -> dict:
    """
    Step 1: Classify the issue
    Step 2: Generate a professional response based on classification
    """
    # Step 1 — Classification chain
    classify_chain = build_chain(CLASSIFY_PROMPT, ["issue"], temperature=0.1)
    classification = classify_chain.invoke({"issue": issue})

    # Step 2 — Response generation chain
    llm = get_llm(temperature=0.6)
    response_prompt = PromptTemplate(
        template=RESPONSE_PROMPT,
        input_variables=["classification", "issue"]
    )
    response_chain = response_prompt | llm | StrOutputParser()
    final_response = response_chain.invoke({
        "classification": classification,
        "issue": issue
    })

    return {
        "classification": classification,
        "response": final_response
    }
