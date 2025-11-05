import streamlit as st


# Page Config
st.set_page_config(page_title="AI Code Assistant", page_icon="💻", layout="centered")

# Header Section
st.title("AI Code Assistant" ,)
st.markdown("""
Welcome to the **AI Code Assistant** your smart helper for reviewing and debugging Python code.  
""")



Code_Debugger = st.Page("Code-Debugger.py", title = "Code-Debugger")
Code_Reviewer = st.Page("Code-Reviewer.py", title = "Code-Reviewer")


pg = st.navigation([Code_Debugger, Code_Reviewer], position="top")

pg.run()


# Footer
st.markdown("---")
st.caption("© 2025 AI Code Assistant | Built with ❤️ using Streamlit")
