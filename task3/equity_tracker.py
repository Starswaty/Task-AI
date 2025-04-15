import yfinance as yf

class ITStockTracker:
    def __init__(self):
        self.symbols = ["INFY.NS", "TCS.NS", "WIPRO.NS", "HCLTECH.NS", "TECHM.NS"]

    def get_latest_prices(self) -> str:
        result = []
        for symbol in self.symbols:
            try:
                ticker = yf.Ticker(symbol)
                hist = ticker.history(period="1d")
                hist.columns = hist.columns.get_level_values(0)

                if not hist.empty:
                    latest_price = hist['Close'].iloc[-1]
                    result.append(f"{symbol} current price = `{latest_price}`")
                else:
                    result.append(f"No data found for {symbol}")
            except Exception as e:
                result.append(f"{symbol} fetch error: {e}")
        return "\n".join(result)


if __name__ == "__main__":
    tracker = ITStockTracker()
    print(tracker.get_latest_prices())
