# 🧠 Smart Workplace Assistant

**A production-grade AI workflow suite built with LangChain, Google Gemini, and Streamlit.**

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)](https://python.org)
[![LangChain](https://img.shields.io/badge/LangChain-LCEL-green?logo=chainlink)](https://langchain.com)
[![Gemini](https://img.shields.io/badge/Google-Gemini%201.5-orange?logo=google)](https://aistudio.google.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-UI-red?logo=streamlit)](https://streamlit.io)

---

## 📌 Overview

The **Smart Workplace Assistant** is a modular, extensible AI system that automates six core workplace workflows using **LangChain LCEL chains** and **Google Gemini** — without relying on `HumanMessage`.

It is built for real-world business scenarios: classifying support tickets, extracting structured data, analyzing employee sentiment, rewriting emails, generating JSON from text, and chaining multiple AI steps together.

---

## ✨ Features

| Module | What It Does |
|---|---|
| 🎫 **Ticket Classifier** | Routes HR / Technical / Finance / General tickets automatically |
| 🔍 **Info Extractor** | Pulls names, dates, tasks, priorities from unstructured text |
| 💬 **Sentiment Analyzer** | Scores feedback as Positive / Negative / Neutral with insights |
| ✉️ **Email Rewriter** | Transforms casual messages into polished professional emails |
| 🗃️ **Structured Output** | Converts any text into clean JSON for automation pipelines |
| ⚡ **Multi-Step Chain** | Chains classification → response generation in one LCEL pipeline |

---

## 🛠️ Technology Stack

- **LangChain** — AI workflow orchestration framework
- **LangChain LCEL** — `prompt | llm | parser` chain syntax
- **Google Gemini 1.5 Flash** — Core language model
- **PromptTemplate** — Dynamic, reusable prompt engineering
- **Streamlit** — Interactive web UI
- **Python 3.9+** — Runtime
- **python-dotenv** — API key management

---

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/your-username/smart-workplace-assistant.git
cd smart-workplace-assistant
```

### 2. Create a virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your API key

```bash
cp .env.example .env
```

Open `.env` and replace the placeholder:

```env
GOOGLE_API_KEY=your_actual_gemini_api_key_here
```

> Get your free API key at [https://aistudio.google.com](https://aistudio.google.com)

### 5. Run the app

```bash
streamlit run app.py
```

Open your browser at **http://localhost:8501**

---

## 📁 Project Structure

```
smart-workplace-assistant/
│
├── app.py                          # Streamlit UI (main entry point)
│
├── src/
│   ├── modules/
│   │   ├── ticket_classifier.py    # Ticket classification chain
│   │   ├── info_extractor.py       # Entity extraction chain
│   │   ├── sentiment_analyzer.py   # Sentiment analysis chain
│   │   ├── email_rewriter.py       # Email rewriting chain
│   │   ├── structured_output.py    # JSON generation chain
│   │   └── multi_step_chain.py     # Multi-step LCEL pipeline (core)
│   │
│   └── utils/
│       └── llm_utils.py            # LLM init, chain builder, shared utils
│
├── .env.example                    # Environment variable template
├── .gitignore                      # Git ignore rules
├── requirements.txt                # Python dependencies
└── README.md                       # This file
```

---

## 🔗 LangChain LCEL Architecture

Every module uses the modern **LangChain Expression Language** pipeline:

```python
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

chain = PromptTemplate(...) | ChatGoogleGenerativeAI(...) | StrOutputParser()
result = chain.invoke({"input": "..."})
```

### Multi-Step Chain (Core Module)

```
User Issue
    │
    ▼
[Chain 1] PromptTemplate → Gemini → Classification Output
    │
    ▼
[Chain 2] Classification + Issue → Gemini → Professional Response
    │
    ▼
Final Output (Classification + Response)
```

---

## 💡 Key Design Decisions

- ✅ **No HumanMessage** — Uses `PromptTemplate` for all structured inputs
- ✅ **LCEL throughout** — Modern `|` pipeline syntax in every module
- ✅ **Modular architecture** — Each feature is an independent, testable module
- ✅ **Single API key** — Only `GOOGLE_API_KEY` required, nothing else
- ✅ **Graceful error handling** — All modules wrapped with try/catch
- ✅ **Download support** — Email and multi-step outputs are downloadable

---

## 🔮 Future Enhancements

- [ ] Conversation memory (LangChain `ConversationBufferMemory`)
- [ ] RAG pipeline with document upload
- [ ] REST API deployment (FastAPI)
- [ ] Database logging of all interactions
- [ ] Batch processing support
- [ ] Authentication and user sessions

---

## 📄 License

MIT License — feel free to use, modify, and distribute.

---

## 🙌 Acknowledgements

- [LangChain](https://langchain.com) — for the powerful chaining framework
- [Google AI Studio](https://aistudio.google.com) — for the Gemini API
- [Streamlit](https://streamlit.io) — for the elegant UI framework

---

> *"We developed a LangChain-based Smart Workplace Assistant using Google Gemini API, leveraging PromptTemplate and LCEL chains to perform classification, extraction, and multi-step workflows without using HumanMessage."*
