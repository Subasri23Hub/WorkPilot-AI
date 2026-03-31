"""
Sentiment Analyzer Module
Analyzes sentiment of employee feedback, reviews, and messages.
"""

from src.utils.llm_utils import build_chain

SENTIMENT_PROMPT = """
You are a professional workplace sentiment analysis engine.

Analyze the sentiment of the following text in a workplace/business context.

Text: {text}

Provide a detailed analysis:

Sentiment: <Positive / Negative / Neutral / Mixed>
Sentiment Score: <score from -1.0 (most negative) to +1.0 (most positive)>
Tone Keywords: <comma-separated list of tone words, e.g., frustrated, hopeful, satisfied>
Key Insight: <One sentence summary of what the person is expressing>
Recommended Action: <What should HR/Management do with this feedback>
"""

def analyze_sentiment(text: str) -> str:
    chain = build_chain(SENTIMENT_PROMPT, ["text"], temperature=0.1)
    return chain.invoke({"text": text})
