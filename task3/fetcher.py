import requests

class FXRateMonitor:
    def __init__(self):
        self.api_token = "your_twelvedata_api_here"
        self.pairs = [("USD", "INR"), ("EUR", "INR"), ("JPY", "INR"), ("CHF", "INR")]

    def get_current_rates(self) -> str:
        output = []
        for from_curr, to_curr in self.pairs:
            endpoint = f"https://api.twelvedata.com/exchange_rate?symbol={from_curr}/{to_curr}&apikey={self.api_token}"
            try:
                res = requests.get(endpoint)
                data = res.json()
                if 'rate' in data:
                    output.append(f"**{from_curr}/{to_curr}** = `{float(data['rate'])}`")
                else:
                    output.append(f"Failed {from_curr}/{to_curr}: {data.get('message', 'No data')}")
            except Exception as err:
                output.append(f"Request error for {from_curr}/{to_curr}: {err}")
        return "\n".join(output)


if __name__ == "__main__":
    fx = FXRateMonitor()
    print(fx.get_current_rates())
