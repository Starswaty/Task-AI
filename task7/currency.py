import requests
import pandas as pd
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("TWELVE_DATA_API_KEY")

def fetch_currency_rates(base='USD', targets=None):
    if targets is None:
        targets = ['INR', 'EUR', 'GBP', 'JPY', 'AUD', 'CAD', 'CHF', 'CNY', 'HKD', 'SGD']

    data = []
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for symbol in targets:
        pair = f"{base}/{symbol}"
        url = f"https://api.twelvedata.com/exchange_rate?symbol={pair}&apikey={API_KEY}"

        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            result = response.json()

            if 'rate' in result:
                data.append({
                    "Pair": pair,
                    "Rate": float(result['rate']),
                    "Timestamp": now
                })
            else:
                print(f"⚠️ Error for {pair}: {result.get('message', 'Unknown error')}")

        except Exception as e:
            print(f"❌ Exception for {pair}: {e}")

    df = pd.DataFrame(data)
    df.to_csv("currencies.csv", index=False)
    return df
