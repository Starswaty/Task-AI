# 📊 PDF Earnings Call Summarizer

A powerful and lightweight tool that extracts and summarizes earnings call transcripts directly from PDF files. Designed for financial analysts, researchers, and investment teams who want fast access to management insights without manually reading lengthy documents.

---

## 🧠 What It Does

This application allows users to upload an earnings call PDF and receive a clean, readable summary that captures key takeaways such as:

- Company performance highlights
- Forward-looking statements from leadership
- Analyst Q&A summaries
- Financial outlook and commentary

The summaries are generated using **Hugging Face's state-of-the-art transformer model** (`facebook/bart-large-cnn`) via API.

---

## 🎯 Why This Matters

Earnings calls are crucial for:
- Gauging company performance
- Understanding management confidence
- Identifying future risks and opportunities

But reading full transcripts (often 10–30 pages) is time-consuming. This app extracts the core insights for rapid consumption.

---

## 💡 Features

 Upload earnings call PDF documents  
 Extract readable text using `pdfplumber`  
 Trim and clean content automatically  
 Summarize using Hugging Face BART model  
 Save summary to a `.txt` file in your local folder  
 Streamlit-powered, modern and responsive UI  
 Secure API key loading with `.env`

---

## 🛠️ Tech Stack

- Python 3.8+
- Streamlit for frontend
- pdfplumber for PDF parsing
- Hugging Face Transformers (via API)
- dotenv for secure key management
- requests for API interaction

---
