from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os
import streamlit as st
 
load_dotenv()

Model_Key = os.getenv("OPEN_ROUTER_KEY")

llm = ChatOpenAI(
    base_url = "https://openrouter.ai/api/v1" ,
    api_key = Model_Key,
    model_name = "openai/gpt-oss-20b"
)

prompt = """You are an AI Code Explainer with deep semantic understanding.
Your goal is to transform complex code into clear, human-readable insight that improves comprehension, maintainability, and developer confidence.
Analyze the provided code without modifying it and produce a structured explanation covering purpose, logic, dependencies, and risks.
Respond strictly in the following format:

Overview:
- State the core intent and responsibility of the code.

Core_Logic:
- Explain how the code works, step by step.
- Highlight key decisions, data flow, and transformations.

Components_And_Dependencies:
- Describe major functions, classes, and external dependencies.
- Explain how components interact.

Patterns_And_Risks:
- Identify design patterns or anti-patterns.
- Flag potential runtime pitfalls, edge cases, or inefficiencies.

Semantic_Interpretation:
- Translate critical code constructs into clear natural-language meaning.

Closing_Insight:
- Provide one or two high-impact insights that help a developer extend, debug, or trust this code.

"""

st.title("Code-Explainer")
st.write("Paste your code below to get feedback.")

# Text area for code input
user_code = st.text_area("Your Code:", height=200, placeholder="Paste your code here...")

# Review button
if st.button("Explain Code"):
    if not user_code.strip():
        st.warning("Please paste some code first.")
    else:
        with st.spinner("Analyzing your code..."):
            response = llm.invoke( f"{prompt}\n\nExplain this code:\n```\n{user_code}\n```")
        st.subheader("Result:")
        st.markdown(response.content)