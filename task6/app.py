import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from data_collector import fetch_stock_data
from data_preprocessor import create_features
from model_trainer import train_model
from visualizer import plot_predictions

st.set_page_config(page_title="IT Stock Forecasting Tool", layout="wide")
st.title("\U0001F4C8 IT Sector Stock Forecasting Tool")

st.sidebar.header("Stock Selector")
stock_options = {
    "TCS": "TCS.NS",
    "Infosys": "INFY.NS",
    "HCL Technologies": "HCLTECH.NS",
    "Wipro": "WIPRO.NS",
    "Tech Mahindra": "TECHM.NS",
    "LTIMindtree": "LTIM.NS",
    "Mphasis": "MPHASIS.NS",
    "Coforge": "COFORGE.NS",
    "Persistent Systems": "PERSISTENT.NS",
    "L&T Technology Services": "LTTS.NS"
}
selected_stock = st.sidebar.selectbox("Choose an IT Stock", options=list(stock_options.keys()))
ticker = stock_options[selected_stock]

start_date = st.sidebar.date_input("Start Date", value=pd.to_datetime("2020-01-01"))
end_date = st.sidebar.date_input("End Date", value=pd.to_datetime("2024-12-31"))


st.text("Fetching data...")
data = fetch_stock_data(ticker=ticker, start=str(start_date), end=str(end_date))
st.success(f"Data fetched for {selected_stock} ({ticker})")

st.subheader("\U0001F50D Raw Stock Data")
st.dataframe(data.tail(10), use_container_width=True)

X, y = create_features(data)
model, X_test, y_test, predictions, rmse, mae, mape, r2 = train_model(X, y)

st.subheader("\U0001F4CA Model Performance Metrics")
col1, col2, col3, col4 = st.columns(4)
col1.metric("RMSE", f"{rmse:.2f}", help="Root Mean Squared Error")
col2.metric("MAE", f"{mae:.2f}", help="Mean Absolute Error")
col3.metric("MAPE", f"{mape:.2f}%", help="Mean Absolute Percentage Error")
col4.metric("R² Score", f"{r2:.2%}", help="Explained variance")

st.subheader("\U0001F4C9 Actual vs Predicted Price")
df_plot = plot_predictions(y_test, predictions)
st.line_chart(df_plot)

st.subheader("\U0001F4CC Next Day Forecast")
latest_features = X.iloc[[-1]]
next_day_prediction = model.predict(latest_features)[0]
st.success(f"Predicted Next Day Close: ₹{next_day_prediction:.2f}")