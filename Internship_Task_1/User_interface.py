import streamlit as st


st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(#EC7491, #EC9474, #EC9474);
    }

        </style>
    """,
    unsafe_allow_html=True)

Explainer = st.Page("Code_Explaination.py", title = "Expaliner")
Generator = st.Page("Code_Generation.py", title = "Generator")
Debugger = st.Page("Debugging_and_Optimization.py", title = "Debugger & Optimization")


pg = st.navigation([Explainer, Generator, Debugger], position="top")


pg.run()
