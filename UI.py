import streamlit as st


# Page Config
st.set_page_config(page_title="AI Code Assistant", page_icon="💻", layout="centered")

st.markdown("""
<style>
            
    /* Set page background color */
    [data-testid="stAppViewContainer"] {
        background-color: #d8e2dc;
    }
    .stTextArea textarea {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.9rem;
    }
    .stButton button {
        background-color: #0066cc;
        color: white;
        border-radius: 8px;
        padding: 0.6rem 1.2rem;
    }
    .stButton button:hover {
        background-color: #0984e3;
    }
</style>
""", unsafe_allow_html=True)



# Header Section
st.title("AI Code Assistant" ,)
st.markdown("""
Welcome to the **AI Code Assistant** your smart helper for reviewing and debugging Python code.  
""")



Code_Debugger = st.Page("Code-Debugger.py", title = "Code-Debugger")
Code_Reviewer = st.Page("Code-Reviewer.py", title = "Code-Reviewer")


pg = st.navigation([Code_Debugger, Code_Reviewer], position="top")

pg.run()

