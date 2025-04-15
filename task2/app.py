import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from tweet_fetcher import fetch_tweets
from sentiment_analyzer import analyze_sentiment
from data_utils import influencers, keywords

st.title("📊 Social Media Sentiment Analyzer for Tech Influencers")

max_tweets = st.slider("Max tweets per query", min_value=10, max_value=100, value=50)

all_data = []

with st.spinner("Fetching and analyzing tweets..."):
    for user in influencers:
        for keyword in keywords:
            tweets = fetch_tweets(user, keyword, max_results=max_tweets)
            for tweet in tweets:
                sentiment = analyze_sentiment(tweet.text)
                all_data.append({
                    "User": user,
                    "Keyword": keyword,
                    "Date": tweet.created_at.date(),
                    "Tweet": tweet.text,
                    "Sentiment": sentiment
                })

df = pd.DataFrame(all_data)

if not df.empty:
    st.success(f"Analyzed {len(df)} tweets ✅")

    st.subheader("Sentiment Breakdown")
    st.write(df["Sentiment"].value_counts())
    fig1, ax1 = plt.subplots()
    df["Sentiment"].value_counts().plot.pie(autopct='%1.1f%%', ax=ax1, colors=["#4caf50", "#f44336", "#ffc107"])
    ax1.set_ylabel("")
    st.pyplot(fig1)

    st.subheader("Sentiment Over Time")
    timeline = df.groupby(['Date', 'Sentiment']).size().unstack().fillna(0)
    st.line_chart(timeline)

    st.subheader("All Tweets")
    st.dataframe(df[['Date', 'User', 'Keyword', 'Tweet', 'Sentiment']])
else:
    st.warning("No tweets found. Try adjusting keywords or influencers.")
