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
You are an AI documentation generator. Your task is to generate clear and concise documentation for the given code. 

Requirements:
1. Add proper docstrings to all functions and classes.
2. Include inline comments for important lines or blocks of code.
3. Provide a 3-4 line plain-language explanation of what the code does.
4. Only work on the provided code; do not add or modify any functionality.
5. Output the result in code format with comments and docstrings included.

"""

st.title("AI Code Document Generator")
st.write("Paste your Python code Here")

user_code = st.text_area("Your Code: ", height=200, placeholder="code here" )

if st.button("Document This Code"):
    if not user_code.strip():
        st.warning("Please enter some code first")
    else:
        with st.spinner("Analyzing your code...."):
            response = llm.invoke(f"{prompt}\n\Document this code:\n'''python\n{user_code}\n'''")
        st.subheader("Results: ")
        st.markdown(response.content)