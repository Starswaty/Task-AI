import yfinance as yf
import pandas as pd

def fetch_it_stocks(tickers, period="1mo", interval="1d"):
    df_all = []
    metadata_all = []

    for ticker in tickers:
        stock = yf.Ticker(ticker)
        hist = stock.history(period=period, interval=interval)
        hist.reset_index(inplace=True)
        hist['Ticker'] = ticker
        df_all.append(hist)

        info = stock.info
        metadata_all.append({
            "Ticker": ticker,
            "Current Price": info.get("currentPrice"),
            "52 Week High": info.get("fiftyTwoWeekHigh"),
            "52 Week Low": info.get("fiftyTwoWeekLow"),
            "Day High": info.get("dayHigh"),
            "Day Low": info.get("dayLow"),
            "Volume": info.get("volume"),
            "Avg Volume": info.get("averageVolume"),
            "Market Cap": info.get("marketCap"),
            "PE Ratio": info.get("trailingPE"),
            "Dividend Yield": info.get("dividendYield"),
            "Sector": info.get("sector")
        })

    df_price = pd.concat(df_all, ignore_index=True)
    df_price.to_csv("stocks.csv", index=False)

    df_meta = pd.DataFrame(metadata_all)
    df_meta.to_csv("stock_metadata.csv", index=False)

    return df_price, df_meta
