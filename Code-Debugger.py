from langchain_openai import ChatOpenAI
import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

Model_Key = os.getenv("OPEN_ROUTER_KEY")


llm = ChatOpenAI(
    base_url = "https://openrouter.ai/api/v1",
    api_key = Model_Key,
    model_name = "openai/gpt-oss-20b:free"
)

prompt = """
You are an AI Code Debugger.

Your task is to thoroughly analyze the provided code snippet and identify any issues that prevent it from running correctly or behaving as intended.

Perform a deep debugging analysis and provide your response strictly in the following structured format:

Logical_Errors:
- List all logical or runtime errors in the code, if any, explaining what causes them and their impact.

Syntax_Errors:
- Identify all syntax or structural issues that would cause the code to fail during execution.

Suggested_Fixes:
- Provide clear, step-by-step solutions or code-level changes to fix each issue and improve reliability, readability, and performance.

Corrected_Code:
- Present the fully corrected and improved version of the code with proper indentation and best practices applied.

"""

st.title("AI Code Debugger")
st.write("Paste your Python code Here")

user_code = st.text_area("Your Code: ", height=200, placeholder="code here")


if st.button("Debug The Code"):
    if not user_code.strip():
        st.warning("Please enter some code first")
    else:
        with st.spinner("Analyzing your code...."):
            response = llm.invoke(f"{prompt}\n\nDebug this code:\n'''python\n{user_code}\n'''")
        st.subheader("Results: ")
        st.markdown(response.content)