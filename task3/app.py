import streamlit as st
import pandas as pd
from fetcher import FXRateMonitor
from equity_tracker import ITStockTracker
from visuals import send_alert,get_percent_change,draw_comparison_chart


st.set_page_config(page_title="Currency Impact Analyzer", layout="wide", page_icon="💹")


st.markdown(
    """
    <h1 style='text-align: center; color: #00FFFF;'>💹 Currency Impact Analyzer for Indian IT Companies</h1>
    <p style='text-align: center; color: gray;'>Track how currency fluctuations affect IT stock prices</p>
    """,
    unsafe_allow_html=True
)


st.sidebar.title("🔧 Tool Options")
selected_tab = st.sidebar.radio("Navigate", ["📈 Live Insights", "📊 Chart Analysis", "⚠️ Alerts"])

fx_tool = FXRateMonitor()
equity_tool = ITStockTracker()


if selected_tab == "📈 Live Insights":
    st.subheader("💱 Current Exchange Rates")
    st.markdown(fx_tool.get_current_rates())

    st.subheader("📉 Today's IT Stock Prices")
    st.markdown(equity_tool.get_latest_prices())


elif selected_tab == "📊 Chart Analysis":
    st.subheader("📊 Historical Trend Analysis")

    exchange_data = pd.DataFrame({
        'Date': pd.date_range(start="2025-04-01", periods=5, freq='D'),
        'Close': [82.5, 83.1, 82.4, 82.9, 83.2]
    }).set_index('Date')

    stock_data = pd.DataFrame({
        'Date': pd.date_range(start="2025-04-01", periods=5, freq='D'),
        'Close': [1200, 1215, 1198, 1210, 1220]
    }).set_index('Date')

    exchange_data = get_percent_change(exchange_data)
    stock_data = get_percent_change(stock_data)


    col1, col2 = st.columns(2)
    with col1:
        st.write("📊 Exchange Rate Changes")
        st.dataframe(exchange_data, use_container_width=True)
    with col2:
        st.write("📉 Stock Price Changes")
        st.dataframe(stock_data, use_container_width=True)

    draw_comparison_chart(exchange_data, stock_data)

elif selected_tab == "⚠️ Alerts":
    st.subheader("⚠️ Set Alert Threshold for Exchange Rate Movements")
    threshold = st.slider("Alert if daily change exceeds (%)", min_value=0.0, max_value=5.0, step=0.5, value=2.0)

    
    latest_change = 2.3  
    st.write(f"🔍 Latest Exchange Rate % Change: `{latest_change}%`")

    if abs(latest_change) > threshold:
        alert_message = f"🚨 Alert: Exchange rate changed by {latest_change:.2f}% (Threshold = {threshold}%)"
        st.error(alert_message)
        send_alert(alert_message)
    else:
        st.success("✅ No alert triggered today.")
