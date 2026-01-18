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

prompt = """You are an AI Debugging and Code Optimization Expert.
Your mission is to identify errors, explain failures clearly, and improve code quality while preserving original behavior.
Analyze the provided code thoroughly, including syntax, semantics, and execution flow. Simulate runtime behavior where necessary.
Respond strictly in the following structured format:

Error_Analysis:
- Identify syntax, semantic, or logical errors.
- Explain the root cause in clear, human-readable terms.

Runtime_Issues:
- Detect potential runtime failures, edge cases, or unstable behavior.
- Describe when and why these issues occur.

Suggested_Fixes:
- Provide precise fixes or safer alternatives.
- Include optimized solutions when applicable.

Optimization_And_Refactoring:
- Recommend refactoring to improve performance, readability, or maintainability.
- Identify redundant code and suggest modularization.

Best_Practices_Alignment:
- Apply language- or framework-specific best practices.
- Highlight improvements that increase long-term scalability and robustness.

Final_Recommendation:
- Summarize the most impactful changes to enhance code reliability and quality.

"""

st.title("Code-Debugger and Optimization")
st.write("Paste your code below and to get feedback.")

# Text area for code input
user_code = st.text_area("Please Enter:", height=200, placeholder="Paste your code here...")

# Review button
if st.button("Review Code"):
    if not user_code.strip():
        st.warning("Please paste some code first.")
    else:
        with st.spinner("Analyzing your code..."):
            response = llm.invoke(f"{prompt}\n\nReview this code:\n```\n{user_code}\n```")
        st.subheader("Result:")
        st.markdown(response.content)