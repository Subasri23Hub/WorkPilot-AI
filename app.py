"""
Smart Workplace Assistant — Streamlit Application
LangChain + Google Gemini | Professional AI Workflow Suite
"""

import streamlit as st
import os
import json
from dotenv import load_dotenv

# ── Page config (must be first Streamlit call) ──────────────────────────────
st.set_page_config(
    page_title="Smart Workplace Assistant",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

load_dotenv()

# ── Custom CSS ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
    /* Main background */
    .stApp { background-color: #0f1117; }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1a1d2e 0%, #0f1117 100%);
        border-right: 1px solid #2d2f3e;
    }

    /* Cards */
    .feature-card {
        background: linear-gradient(135deg, #1e2235 0%, #252840 100%);
        border: 1px solid #3d4063;
        border-radius: 12px;
        padding: 1.4rem 1.6rem;
        margin-bottom: 1rem;
        transition: border-color 0.2s;
    }
    .feature-card:hover { border-color: #6c63ff; }

    /* Output box */
    .output-box {
        background: #1a1d2e;
        border: 1px solid #3d4063;
        border-left: 4px solid #6c63ff;
        border-radius: 8px;
        padding: 1.2rem 1.4rem;
        font-family: 'Courier New', monospace;
        font-size: 0.88rem;
        white-space: pre-wrap;
        color: #e0e0f0;
        line-height: 1.7;
    }

    /* Step badges */
    .step-badge {
        display: inline-block;
        background: #6c63ff;
        color: white;
        border-radius: 20px;
        padding: 2px 14px;
        font-size: 0.78rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }

    /* Metric cards */
    div[data-testid="metric-container"] {
        background: #1e2235;
        border: 1px solid #3d4063;
        border-radius: 10px;
        padding: 0.6rem 1rem;
    }

    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #6c63ff, #4f46e5);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.5rem 2rem;
        font-weight: 600;
        transition: opacity 0.2s;
    }
    .stButton > button:hover { opacity: 0.85; }

    /* Headers */
    h1, h2, h3 { color: #e8e8ff !important; }

    /* Tab styling */
    .stTabs [data-baseweb="tab"] {
        color: #9090b8;
        font-weight: 500;
    }
    .stTabs [aria-selected="true"] {
        color: #6c63ff !important;
        border-bottom-color: #6c63ff !important;
    }

    /* Spinner */
    .stSpinner > div { border-top-color: #6c63ff !important; }
</style>
""", unsafe_allow_html=True)


# ── API Key check helper ─────────────────────────────────────────────────────
def check_api_key() -> bool:
    key = os.getenv("GOOGLE_API_KEY", "")
    return bool(key and key != "your_gemini_api_key_here")


# ── Sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🧠 Smart Workplace\n### Assistant")
    st.markdown("---")

    # API key input
    st.markdown("#### 🔑 API Configuration")
    api_key_input = st.text_input(
        "Google Gemini API Key",
        type="password",
        placeholder="AIza...",
        help="Get your key from https://aistudio.google.com",
    )
    if api_key_input:
        os.environ["GOOGLE_API_KEY"] = api_key_input
        st.success("✅ API Key loaded!")
    elif check_api_key():
        st.success("✅ API Key found in .env!")
    else:
        st.warning("⚠️ Please enter your Gemini API Key")

    st.markdown("---")
    st.markdown("#### 🗂️ Modules")
    st.markdown("""
- 🎫 Ticket Classifier
- 🔍 Info Extractor
- 💬 Sentiment Analyzer
- ✉️ Email Rewriter
- 🗃️ Structured Output
- ⚡ Multi-Step Chain
    """)

    st.markdown("---")
    st.markdown("#### 🛠️ Stack")
    st.markdown("""
`LangChain` · `Google Gemini`  
`LCEL Chains` · `PromptTemplate`  
`Streamlit` · `Python`
    """)
    st.markdown("---")
    st.caption("v1.0.0 · Built with ❤️ using LangChain + Gemini")


# ── Hero Header ──────────────────────────────────────────────────────────────
st.markdown("""
<div style='text-align:center; padding: 2rem 0 1rem 0;'>
    <h1 style='font-size:2.8rem; font-weight:800; background: linear-gradient(90deg,#6c63ff,#a78bfa); -webkit-background-clip:text; -webkit-text-fill-color:transparent;'>
        🧠 Smart Workplace Assistant
    </h1>
    <p style='color:#9090b8; font-size:1.1rem; margin-top:0.3rem;'>
        Powered by LangChain · Google Gemini · LCEL Chains
    </p>
</div>
""", unsafe_allow_html=True)

# Metrics row
col1, col2, col3, col4 = st.columns(4)
col1.metric("🔗 LangChain", "LCEL Chains")
col2.metric("🤖 Model", "Gemini 1.5 Flash")
col3.metric("📦 Modules", "6 AI Tools")
col4.metric("💡 Use Cases", "Real-World")

st.markdown("---")


# ── Tabs ─────────────────────────────────────────────────────────────────────
tabs = st.tabs([
    "🎫 Ticket Classifier",
    "🔍 Info Extractor",
    "💬 Sentiment Analyzer",
    "✉️ Email Rewriter",
    "🗃️ Structured Output",
    "⚡ Multi-Step Chain",
    "📘 About",
])


# ═══════════════════════════════════════════════════════════════════════════════
# TAB 1 — TICKET CLASSIFIER
# ═══════════════════════════════════════════════════════════════════════════════
with tabs[0]:
    st.markdown("### 🎫 Support Ticket Classifier")
    st.markdown("Automatically routes support tickets to the correct department using AI.")

    examples = {
        "Custom": "",
        "IT Issue": "My laptop won't connect to the office Wi-Fi and I've missed two meetings.",
        "HR Query": "I need to check my remaining annual leave balance for this financial year.",
        "Finance": "My travel reimbursement claim from last month has not been processed yet.",
        "General": "Can someone tell me the cafeteria menu for this week?",
    }

    col_a, col_b = st.columns([3, 1])
    with col_b:
        selected = st.selectbox("📋 Load Example", list(examples.keys()))
    with col_a:
        ticket_text = st.text_area(
            "Enter Support Ticket",
            value=examples[selected],
            height=130,
            placeholder="Describe the employee issue or support request...",
        )

    if st.button("🚀 Classify Ticket", key="classify"):
        if not check_api_key():
            st.error("❌ Please enter your Gemini API Key in the sidebar.")
        elif not ticket_text.strip():
            st.warning("Please enter a ticket description.")
        else:
            with st.spinner("🔍 Analyzing ticket..."):
                try:
                    from src.modules.ticket_classifier import classify_ticket
                    result = classify_ticket(ticket_text)
                    st.markdown("#### 📊 Classification Result")
                    st.markdown(f'<div class="output-box">{result}</div>', unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"Error: {e}")


# ═══════════════════════════════════════════════════════════════════════════════
# TAB 2 — INFO EXTRACTOR
# ═══════════════════════════════════════════════════════════════════════════════
with tabs[1]:
    st.markdown("### 🔍 Information Extractor")
    st.markdown("Extracts structured entities — names, dates, tasks, priorities — from unstructured workplace text.")

    ie_examples = {
        "Custom": "",
        "Meeting Note": "Please remind John to submit the Q3 report by Friday 14th. Sarah will review it on Monday morning.",
        "Task Assignment": "Alex needs to deploy the new payment module to production by end of next week. High priority.",
        "Email Snippet": "Hi team, Priya from Marketing has scheduled the product launch review for 22nd July at 3 PM.",
    }

    col_a, col_b = st.columns([3, 1])
    with col_b:
        ie_selected = st.selectbox("📋 Load Example", list(ie_examples.keys()), key="ie_ex")
    with col_a:
        ie_text = st.text_area(
            "Enter Workplace Text",
            value=ie_examples[ie_selected],
            height=130,
            placeholder="Paste meeting notes, emails, or task descriptions...",
        )

    if st.button("🔎 Extract Information", key="extract"):
        if not check_api_key():
            st.error("❌ Please enter your Gemini API Key in the sidebar.")
        elif not ie_text.strip():
            st.warning("Please enter some text.")
        else:
            with st.spinner("📡 Extracting entities..."):
                try:
                    from src.modules.info_extractor import extract_info
                    result = extract_info(ie_text)
                    st.markdown("#### 📋 Extracted Information")
                    st.markdown(f'<div class="output-box">{result}</div>', unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"Error: {e}")


# ═══════════════════════════════════════════════════════════════════════════════
# TAB 3 — SENTIMENT ANALYZER
# ═══════════════════════════════════════════════════════════════════════════════
with tabs[2]:
    st.markdown("### 💬 Sentiment Analyzer")
    st.markdown("Analyze employee feedback, survey responses, and workplace communications.")

    sa_examples = {
        "Custom": "",
        "Positive Feedback": "I'm really enjoying the new project management system. It has made collaboration so much easier!",
        "Negative Feedback": "I've been waiting three weeks for my equipment request to be approved. This is extremely frustrating.",
        "Mixed Review": "The new office is great but the commute has become really difficult for most of the team.",
        "Neutral Survey": "The training was completed as scheduled. Attendance was average and the material was covered.",
    }

    col_a, col_b = st.columns([3, 1])
    with col_b:
        sa_selected = st.selectbox("📋 Load Example", list(sa_examples.keys()), key="sa_ex")
    with col_a:
        sa_text = st.text_area(
            "Enter Feedback or Message",
            value=sa_examples[sa_selected],
            height=130,
            placeholder="Paste employee feedback, review, or any workplace message...",
        )

    if st.button("💡 Analyze Sentiment", key="sentiment"):
        if not check_api_key():
            st.error("❌ Please enter your Gemini API Key in the sidebar.")
        elif not sa_text.strip():
            st.warning("Please enter some text.")
        else:
            with st.spinner("🧠 Processing sentiment..."):
                try:
                    from src.modules.sentiment_analyzer import analyze_sentiment
                    result = analyze_sentiment(sa_text)
                    st.markdown("#### 📈 Sentiment Analysis")
                    st.markdown(f'<div class="output-box">{result}</div>', unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"Error: {e}")


# ═══════════════════════════════════════════════════════════════════════════════
# TAB 4 — EMAIL REWRITER
# ═══════════════════════════════════════════════════════════════════════════════
with tabs[3]:
    st.markdown("### ✉️ Professional Email Rewriter")
    st.markdown("Transform informal messages into polished, professional business emails.")

    er_examples = {
        "Custom": "",
        "Leave Request": "hey boss i wanna take leave next week friday and monday. got some personal stuff to handle. let me know if its ok",
        "Bug Report": "the login page is broken again and users cant get in. we need to fix this asap before tomorrow morning",
        "Meeting Request": "can we meet sometime this week to talk about the budget for next quarter? i have some ideas",
    }

    col_a, col_b = st.columns([3, 1])
    with col_b:
        er_selected = st.selectbox("📋 Load Example", list(er_examples.keys()), key="er_ex")

    col_c, col_d, col_e = st.columns([3, 1, 1])
    with col_c:
        er_text = st.text_area(
            "Enter Informal Message",
            value=er_examples[er_selected],
            height=130,
            placeholder="Type or paste your casual message here...",
        )
    with col_d:
        recipient = st.selectbox("Recipient", ["Manager", "HR Team", "Client", "Team", "CEO", "Vendor"])
    with col_e:
        tone = st.selectbox("Tone", ["Formal", "Semi-Formal", "Polite", "Assertive", "Apologetic"])

    if st.button("✍️ Rewrite Email", key="email"):
        if not check_api_key():
            st.error("❌ Please enter your Gemini API Key in the sidebar.")
        elif not er_text.strip():
            st.warning("Please enter a message to rewrite.")
        else:
            with st.spinner("✨ Crafting professional email..."):
                try:
                    from src.modules.email_rewriter import rewrite_email
                    result = rewrite_email(er_text, recipient, tone)
                    st.markdown("#### 📧 Professional Email")
                    st.markdown(f'<div class="output-box">{result}</div>', unsafe_allow_html=True)
                    st.download_button("⬇️ Download Email", result, file_name="professional_email.txt")
                except Exception as e:
                    st.error(f"Error: {e}")


# ═══════════════════════════════════════════════════════════════════════════════
# TAB 5 — STRUCTURED OUTPUT
# ═══════════════════════════════════════════════════════════════════════════════
with tabs[4]:
    st.markdown("### 🗃️ Structured Output Generator")
    st.markdown("Convert free-form workplace text into clean JSON for analytics pipelines and automation.")

    so_examples = {
        "Custom": ("", "general text"),
        "Meeting Notes": (
            "Sprint planning meeting on July 15. Attendees: Dev team, PM Rahul. "
            "Decided to prioritize the payment gateway fix. Action: Dev team to deliver by July 20. "
            "Next meeting July 22.",
            "meeting note"
        ),
        "Incident Report": (
            "On 10th July at 2PM the production server went down due to a memory leak in the auth service. "
            "Reported by DevOps engineer Kiran. Severity: Critical. Resolved by restarting the service at 2:45PM.",
            "incident report"
        ),
        "Task Description": (
            "Arjun needs to build the new user dashboard for the admin panel. "
            "Due date is next Friday. This is a high priority task and depends on the API team finishing their endpoints first.",
            "task description"
        ),
    }

    col_a, col_b = st.columns([3, 1])
    with col_b:
        so_selected = st.selectbox("📋 Load Example", list(so_examples.keys()), key="so_ex")
    with col_a:
        so_text = st.text_area(
            "Enter Workplace Text",
            value=so_examples[so_selected][0],
            height=130,
            placeholder="Paste any unstructured workplace text...",
        )

    doc_type = st.selectbox(
        "Document Type",
        ["general text", "meeting note", "incident report", "task description"],
        index=["general text", "meeting note", "incident report", "task description"].index(
            so_examples[so_selected][1]
        ),
    )

    if st.button("⚙️ Generate JSON", key="structured"):
        if not check_api_key():
            st.error("❌ Please enter your Gemini API Key in the sidebar.")
        elif not so_text.strip():
            st.warning("Please enter some text.")
        else:
            with st.spinner("🔧 Structuring data..."):
                try:
                    from src.modules.structured_output import generate_structured_output
                    result = generate_structured_output(so_text, doc_type)
                    st.markdown("#### 📦 Structured JSON Output")
                    # Try to pretty-print JSON
                    try:
                        clean = result.strip().lstrip("```json").lstrip("```").rstrip("```").strip()
                        parsed = json.loads(clean)
                        st.json(parsed)
                    except Exception:
                        st.markdown(f'<div class="output-box">{result}</div>', unsafe_allow_html=True)
                    st.download_button("⬇️ Download JSON", result, file_name="structured_output.json")
                except Exception as e:
                    st.error(f"Error: {e}")


# ═══════════════════════════════════════════════════════════════════════════════
# TAB 6 — MULTI-STEP CHAIN
# ═══════════════════════════════════════════════════════════════════════════════
with tabs[5]:
    st.markdown("### ⚡ Multi-Step Chain — Core LangChain Showcase")
    st.markdown("""
    This module demonstrates **LangChain LCEL chaining** — the output of one chain feeds into the next.
    
    > **Step 1** → Classify the issue  
    > **Step 2** → Generate a professional response *based on the classification*
    """)

    ms_examples = {
        "Custom": "",
        "IT Urgency": "My entire team cannot access the internal dashboard since this morning. We have a client demo in 2 hours.",
        "HR Conflict": "I feel I was passed over for the promotion unfairly. I have better performance ratings than the person who was promoted.",
        "Finance Delay": "My expense reimbursement for the business trip in May has still not been credited to my account.",
        "General Concern": "The office pantry has been out of coffee for a week and people are getting frustrated.",
    }

    col_a, col_b = st.columns([3, 1])
    with col_b:
        ms_selected = st.selectbox("📋 Load Example", list(ms_examples.keys()), key="ms_ex")
    with col_a:
        ms_issue = st.text_area(
            "Enter Employee Issue",
            value=ms_examples[ms_selected],
            height=130,
            placeholder="Describe any workplace problem or concern...",
        )

    if st.button("⚡ Run Multi-Step Chain", key="multistep"):
        if not check_api_key():
            st.error("❌ Please enter your Gemini API Key in the sidebar.")
        elif not ms_issue.strip():
            st.warning("Please enter an issue.")
        else:
            with st.spinner("🔗 Running LangChain multi-step pipeline..."):
                try:
                    from src.modules.multi_step_chain import run_multi_step_chain
                    result = run_multi_step_chain(ms_issue)

                    col_x, col_y = st.columns(2)
                    with col_x:
                        st.markdown('<span class="step-badge">STEP 1 — Classification</span>', unsafe_allow_html=True)
                        st.markdown(f'<div class="output-box">{result["classification"]}</div>', unsafe_allow_html=True)
                    with col_y:
                        st.markdown('<span class="step-badge">STEP 2 — AI Response</span>', unsafe_allow_html=True)
                        st.markdown(f'<div class="output-box">{result["response"]}</div>', unsafe_allow_html=True)

                    full_output = f"=== CLASSIFICATION ===\n{result['classification']}\n\n=== RESPONSE ===\n{result['response']}"
                    st.download_button("⬇️ Download Full Output", full_output, file_name="multi_step_output.txt")
                except Exception as e:
                    st.error(f"Error: {e}")


# ═══════════════════════════════════════════════════════════════════════════════
# TAB 7 — ABOUT
# ═══════════════════════════════════════════════════════════════════════════════
with tabs[6]:
    st.markdown("### 📘 About This Project")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
<div class="feature-card">
<h4>🎯 Project Goal</h4>
<p>Build a production-grade AI workplace assistant using LangChain and Google Gemini — 
without HumanMessage — demonstrating real-world PromptTemplate and LCEL chain workflows.</p>
</div>

<div class="feature-card">
<h4>🔗 LangChain LCEL</h4>
<p>Every module uses the modern LangChain Expression Language pipeline syntax:<br>
<code>prompt | llm | StrOutputParser()</code><br>
This enables composable, readable, and highly scalable AI workflows.</p>
</div>

<div class="feature-card">
<h4>⚡ Multi-Step Chain</h4>
<p>The core module chains two LLM calls sequentially — classification output feeds directly 
into the response generator — showcasing true workflow automation.</p>
</div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
<div class="feature-card">
<h4>🛠️ Technology Stack</h4>
<ul>
<li><strong>LangChain</strong> — AI workflow framework</li>
<li><strong>Google Gemini 1.5 Flash</strong> — Core LLM</li>
<li><strong>LCEL</strong> — Chain expression language</li>
<li><strong>PromptTemplate</strong> — Dynamic prompt engineering</li>
<li><strong>Streamlit</strong> — UI framework</li>
<li><strong>Python + dotenv</strong> — Runtime & config</li>
</ul>
</div>

<div class="feature-card">
<h4>📦 Modules</h4>
<ul>
<li>🎫 <strong>Ticket Classifier</strong> — HR / Tech / Finance / General</li>
<li>🔍 <strong>Info Extractor</strong> — Name, date, task, priority</li>
<li>💬 <strong>Sentiment Analyzer</strong> — Positive / Negative / Neutral</li>
<li>✉️ <strong>Email Rewriter</strong> — Informal → Professional</li>
<li>🗃️ <strong>Structured Output</strong> — Text → JSON</li>
<li>⚡ <strong>Multi-Step Chain</strong> — Sequential AI reasoning</li>
</ul>
</div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("""
> **One-line summary:**  
> *"A LangChain-based Smart Workplace Assistant using Google Gemini, leveraging PromptTemplate and LCEL chains 
> to perform classification, extraction, sentiment analysis, email rewriting, structured output generation, 
> and multi-step reasoning workflows — without HumanMessage."*
    """)
