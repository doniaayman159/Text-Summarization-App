from transformers import pipeline

text_summarization = pipeline('summarization')


import streamlit as st
from io import StringIO



# Title
st.title("📄 Text Summarization App")
st.markdown("This app summarizes large text using Hugging Face Transformers.")

# Sidebar controls
st.sidebar.header("Settings")
min_length = st.sidebar.slider("Minimum summary length", 20, 200, 50)
max_length = st.sidebar.slider("Maximum summary length", 50, 500, 150)

# Input method
input_option = st.radio("Choose input method", ["Text box", "Upload file"])

# Get input text
input_text = ""

if input_option == "Text box":
    input_text = st.text_area("Enter your text here:", height=300)
else:
    uploaded_file = st.file_uploader("Upload a .txt file", type=["txt"])
    if uploaded_file is not None:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        input_text = stringio.read()

# Summarize button
if st.button("Summarize"):
    if input_text:
        with st.spinner("Summarizing..."):
            summary = text_summarization(input_text, min_length=min_length, max_length=max_length, do_sample=False)
            st.subheader("Summary:")
            st.success(summary[0]['summary_text'])
    else:
        st.warning("Please enter or upload some text.")