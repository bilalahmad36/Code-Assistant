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

prompt = """You are an AI Code Generator powered by transformer-based models.
Your task is to convert natural language requirements into correct, efficient, and readable source code while preserving intent and best practices.
Generate code based strictly on the user’s description and apply language-appropriate conventions.
Follow this structured output format:

Problem_Interpretation:
- Briefly restate the user’s requirement to confirm intent.

Language_And_Environment:
- Specify the target programming language and relevant assumptions.

Generated_Code:
- Produce clean, executable code that fulfills the requirement.
- Ensure modular structure and meaningful naming.
- Dont include explanations or comments in this section.
- Generate concise and precise code
- Give proper indentation based code structure.

Implementation_Notes:
- Highlight key design decisions or trade-offs.

"""

st.title("Code-Generator")
st.write("Enter your requirements below to get source code.")

# Text area for code input
user_code = st.text_area("Enter:", height=100)

# Review button
if st.button("Generate Code"):
    if not user_code.strip():
        st.warning("Please paste some Text first.")
    else:
        with st.spinner("Generating..."):
            response = llm.invoke(f"{prompt}\n\nGenerate the code:\n```\n{user_code}\n```")
        st.subheader("Result:")
        st.markdown(response.content)