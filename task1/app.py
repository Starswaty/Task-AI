import streamlit as st
from scrapper import fetch_top_news
from summarizer import summarize_article

st.set_page_config(page_title="📰 Tech News Summarizer", layout="wide")

st.markdown("""
    <style>
        .main {
            background-color: #f9f9f9;
            padding: 2rem;
        }
        .title {
            font-size: 2.2rem;
            font-weight: bold;
            color: #2e7bcf;
            margin-bottom: 1rem;
        }
        .subheader {
            font-size: 1.2rem;
            color: #666;
            margin-bottom: 2rem;
        }
        .article-box {
            background-color: white;
            padding: 1rem;
            border-radius: 10px;
            box-shadow: 0px 2px 5px rgba(0,0,0,0.1);
            margin-bottom: 1rem;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🧠 Tech News Summarizer</div>', unsafe_allow_html=True)
st.markdown('<div class="subheader">Choose a tech headline or summarize all top stories</div>', unsafe_allow_html=True)

# Fetch top news
news_items = fetch_top_news()

if not news_items:
    st.error("❌ Couldn't fetch tech news. Please try again later.")
else:
    news_titles = [item["title"] for item in news_items]
    selected_title = st.selectbox("🔎 Choose a headline to summarize", [""] + news_titles)

    if selected_title:
        selected_article = next(item for item in news_items if item["title"] == selected_title)
        st.markdown(f"### 📰 {selected_article['title']}")
        st.markdown(f"🔗 [Read Full Article]({selected_article['link']})")
        
        if st.button("📌 Summarize This Article"):
            with st.spinner("Summarizing..."):
                summary = summarize_article(selected_article["link"])
                if summary:
                    st.success("✅ Summary Generated")
                    st.markdown(f"**Summary:**\n\n{summary}")
                else:
                    st.error("⚠️ Summarization failed. Try another article.")

    st.markdown("---")
    if st.button("📝 Summarize All Articles"):
        st.markdown("### 🧾 All News Summaries")
        for item in news_items:
            with st.spinner(f"Summarizing: {item['title']}"):
                summary = summarize_article(item["link"])
                if summary:
                    st.markdown(f'<div class="article-box"><b>{item["title"]}</b><br><br>{summary}<br><a href="{item["link"]}" target="_blank">Read full</a></div>', unsafe_allow_html=True)
                else:
                    st.warning(f"⚠️ Couldn’t summarize: {item['title']}")
