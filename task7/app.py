import streamlit as st
import pandas as pd
import plotly.express as px

from stocks import fetch_it_stocks
from currency import fetch_currency_rates
from news import fetch_tech_news
from exporter import export_data

st.set_page_config(layout="wide", page_title="IT Sector Financial Dashboard")
st.title("📊 IT Sector Financial Dashboard")


st.sidebar.title("🔍 Filters")
tickers = ['INFY.NS', 'TCS.NS', 'WIPRO.NS', 'HCLTECH.NS', 'TECHM.NS', 'LTIM.NS', 'COFORGE.NS', 'MPHASIS.NS']
selected_ticker = st.sidebar.selectbox("Choose Company", ["All"] + tickers)


top_currencies = ['INR', 'EUR', 'GBP', 'JPY', 'AUD', 'CAD', 'CHF', 'CNY', 'HKD', 'SGD']
selected_base = st.sidebar.selectbox("Base Currency", ['USD'])
selected_targets = st.sidebar.multiselect("Target Currencies", top_currencies, default=['INR'])

with st.spinner("Fetching latest data..."):
    df_stocks,df_metadata = fetch_it_stocks(tickers)
    df_currency = fetch_currency_rates(base=selected_base, targets=selected_targets)
    df_news = fetch_tech_news()


tab1, tab2, tab3 = st.tabs(["📈 Stock Performance", "💱 Currency Rates", "📰 News Feed"])

with tab1:
    st.subheader("📈 IT Company Stock Prices")

    if selected_ticker != "All":
        filtered = df_stocks[df_stocks['Ticker'] == selected_ticker]
        meta = df_metadata[df_metadata['Ticker'] == selected_ticker]
    else:
        filtered = df_stocks
        meta = df_metadata

    st.markdown("### 📊 Stock Price Chart")
    fig = px.line(filtered, x="Date", y="Close", color="Ticker", title="Stock Price Trend")
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("### 📘 Stock Details")
    st.dataframe(meta, use_container_width=True)

    st.download_button("📥 Export Stock Prices", data=filtered.to_csv(index=False), file_name="stock_data.csv")
    st.download_button("📥 Export Stock Info", data=meta.to_csv(index=False), file_name="stock_info.csv")


with tab2:
    st.subheader(f"💱 Currency Exchange Rates (Base: {selected_base})")
    st.dataframe(df_currency, use_container_width=True)
    st.download_button("📥 Export Currency Data", data=df_currency.to_csv(index=False), file_name="currency_data.csv")


with tab3:
    st.subheader("📰 Latest Tech News")
    for _, row in df_news.iterrows():
        st.markdown(f"**{row['Title']}**  ")
        st.markdown(f"Published: {row['Published']} | Source: {row['Source']}")
        st.markdown(f"[Read more]({row['Link']})")
        st.markdown("---")
    st.download_button("📥 Export News Feed", data=df_news.to_csv(index=False), file_name="tech_news.csv")
