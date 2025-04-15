import pandas as pd

def export_data(filename):
    try:
        return pd.read_csv(f"data/{filename}")
    except Exception as e:
        return pd.DataFrame([{"Error": str(e)}])

