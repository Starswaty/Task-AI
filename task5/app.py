import streamlit as st
from pdf_extractor import extract_text_from_pdf
from summarizer import generate_summary

st.set_page_config(page_title="Earnings Call Summarizer", layout="wide")

st.title("📄 Earnings Call PDF Summarizer")
st.write("Upload an earnings call transcript (PDF) and get a short summary.")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    st.info("Extracting text from PDF...")
    text = extract_text_from_pdf("temp.pdf")
    
    if text:
        with st.expander("📘 Extracted Text"):
            st.text_area("Text", text, height=300)

        st.info("Generating summary...")
        summary = generate_summary(text)

        st.subheader("📝 Summary")
        st.write(summary)
        
        if st.button("Download Summary"):
            with open("summary.txt", "w") as f:
                f.write(summary)
            st.success("Summary saved as summary.txt")
    else:
        st.warning("No text could be extracted from the PDF.")
