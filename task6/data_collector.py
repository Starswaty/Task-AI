import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker, start="2020-01-01", end="2024-12-31"):
    data = yf.download(ticker, start=start, end=end)
    data = data[['Open', 'High', 'Low', 'Close', 'Volume']]
    data.dropna(inplace=True)
    return data
