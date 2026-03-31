"""
LLM initialization and shared utilities for the Smart Workplace Assistant.
"""

import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

def get_llm(temperature: float = 0.3) -> ChatGoogleGenerativeAI:
    """Initialize and return the Google Gemini LLM."""
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY not found. Please set it in your .env file.")
    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=api_key,
        temperature=temperature,
    )

def build_chain(prompt_template: str, input_variables: list, temperature: float = 0.3):
    """Build a reusable LangChain LCEL chain."""
    llm = get_llm(temperature)
    prompt = PromptTemplate(template=prompt_template, input_variables=input_variables)
    parser = StrOutputParser()
    return prompt | llm | parser
