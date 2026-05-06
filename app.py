import streamlit as st
from utils import get_ai_response
from prompts import get_prompt

st.set_page_config(page_title="AI Code Explainer Pro", layout="wide")

# Custom Styling
st.markdown("""
<style>
.block-container {
    padding-top: 2rem;
}
textarea {
    font-family: monospace;
}
</style>
""", unsafe_allow_html=True)

# Header
st.title("🧠 AI Code Explainer Pro")
st.caption("Powered by Groq ⚡ | Fast AI Code Understanding")

# Layout
col1, col2 = st.columns([1, 1])

# LEFT PANEL
with col1:
    st.subheader("💻 Code Input")

    code = st.text_area("Paste your code here", height=400)

    language = st.selectbox(
        "Language",
        ["Python", "Java", "JavaScript", "C++", "Other"]
    )

    mode = st.radio(
        "Mode",
        ["Beginner", "Advanced", "Debug"]
    )

    explain = st.button("🚀 Explain Code")

# RIGHT PANEL
with col2:
    st.subheader("📖 Output")

    if explain:
        if not code.strip():
            st.warning("Please enter some code.")
        else:
            with st.spinner("⚡ Groq is thinking..."):
                prompt = get_prompt(code, mode)
                result = get_ai_response(prompt)

                st.success("Done!")
                st.write(result)

# Divider
st.markdown("---")

# CHAT SECTION
st.subheader("💬 Chat with Your Code")

if "history" not in st.session_state:
    st.session_state.history = []

question = st.text_input("Ask a question about your code...")

if st.button("Ask"):
    if question and code:
        chat_prompt = f"""
You are a coding assistant.

Code:
{code}

User Question:
{question}
"""
        answer = get_ai_response(chat_prompt)

        st.session_state.history.append(("You", question))
        st.session_state.history.append(("AI", answer))

# Display Chat
for role, msg in st.session_state.history:
    if role == "You":
        st.markdown(f"**🧑 {msg}**")
    else:
        st.markdown(f"**🤖 {msg}**")

# Footer
st.markdown("---")
st.caption("⚡ Built with Groq + Streamlit")