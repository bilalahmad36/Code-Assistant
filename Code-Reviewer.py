from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os
import streamlit as st
 
load_dotenv()

Model_Key = os.getenv("OPEN_ROUTER_KEY")

llm = ChatOpenAI(
    base_url = "https://openrouter.ai/api/v1" ,
    api_key = Model_Key,
    model_name = "deepseek/deepseek-r1-0528-qwen3-8b:free"
)

prompt = """You are an AI Code Reviewer.

Your task is to carefully analyze the provided code snippet and evaluate it for correctness, readability, efficiency, and potential errors.

After a deep analysis, produce your response in the following structured format:

Summary:
- Provide a concise explanation of what the code does.

Potential_Issues:
- List any logical errors, syntax problems, or bad practices found in the code.

Suggestions:
- Offer clear and actionable recommendations for improving performance, clarity, or maintainability.

"""

st.title("AI Code Reviewer")
st.write("Paste your Python code below and click **Review Code** to get AI feedback.")

# Text area for code input
user_code = st.text_area("Your Code:", height=200, placeholder="Paste your Python code here...")

# Review button
if st.button("Review Code"):
    if not user_code.strip():
        st.warning("Please paste some code first.")
    else:
        with st.spinner("Analyzing your code..."):
            response = llm.invoke(f"{prompt}\n\nReview this code:\n```python\n{user_code}\n```")
        st.subheader("Review Result:")
        st.markdown(response.content)