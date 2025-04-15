#  Project - Task 1 to Task 7 (Internship Assignments)

## 📌 Overview

This repository contains **seven fully completed  and tested(on local machine) tasks** as part of a internship selection project. Each task is self-contained and includes all necessary scripts, a `requirements.txt`, and example screenshots to demonstrate successful execution.

Each task is structured in its own folder:

```
📁 Project/
├── task1_it_news_aggregator/
├── task2_sentiment_analyzer/
├── task3_currency_impact_analyzer/
├── task4_scraper_financial_updates/
├── task5_pdf_earnings_summarizer/
├── task6_stock_forecasting/
├── task7_financial_dashboard/
```

Each folder includes:
- ✅ Well-documented and modular Python code
- ✅ Required dependencies in `requirements.txt`
- ✅ Streamlit or CLI interfaces
- ✅ Output screenshots
- ✅ `.env` (optional, if APIs are used)

---

## 🚀 How to Run Any Task

### 🔧 Step-by-step Instructions:

1. **Clone the repository**

```bash
git clone https://github.com/ashutoshbins/Project.git
cd Project
```

2. **Navigate to the task folder you want to run**

```bash
cd tasknumber   # ex. task2, task3, etc.
```

3. **Install the required dependencies**

```bash
pip install -r requirements.txt
```

4. **Set up `.env` file** (only for tasks that require API keys)

Create a `.env` file in the root of the task folder and add the relevant keys:

```env
HUGGINGFACE_API_TOKEN=your_token_here
TWITTER_BEARER_TOKEN=your_twitter_token_here
```

5. **Run the Streamlit app** (if applicable)

```bash
streamlit run app.py
```

---

## 📚 Task Summaries

### ✅ Task 1 - IT & Tech Deal News Aggregator
- Scrapes tech deal news from Economic Times RSS feed
- Summarizes articles using Hugging Face API
- Beautiful, interactive Streamlit UI with dropdown selection

### ✅ Task 2 - Social Media Sentiment Analyzer
- Uses Twitter API and Tweepy
- Fetches tweets of macro influencers
- Analyzes sentiment using VADER/TextBlob
- Streamlit app with stylish dark mode UI

### ✅ Task 3 - Currency Impact Analyzer
- Tracks exchange rates (USD/INR, EUR/INR, etc.)
- Compares impact on top Indian IT stock indices
- Shows graphs + alerts for user-defined thresholds

### ✅ Task 4 - Web Scraper for Financial Updates
- Scrapes financial news and investor updates from 5 websites
- Cleans and displays top headlines (title, source, link)
- Streamlit table output

### ✅ Task 5 - PDF Earnings Call Summarizer
- Parses earnings report PDFs
- Summarizes key financial insights
- Option to export or email summaries

### ✅ Task 6 - Stock Movement Forecasting
- Predicts next-day stock direction using regression
- Visualizes predictions and trends with Streamlit
- Clean graphs and high accuracy model

### ✅ Task 7 - Financial Dashboard for IT Sector
- Combines currency, news, stock data in one dashboard
- Realtime data + visual metrics
- Streamlit UI with responsive layout and filters

---

## 🛠️ Technologies Used

- Python 3.x
- Streamlit
- BeautifulSoup
- Hugging Face Transformers
- Tweepy (Twitter API)
- VADER / TextBlob
- Requests / Regex / Pandas
- Scikit-learn
- pdfplumber
- dotenv

---
