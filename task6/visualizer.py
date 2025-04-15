import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_predictions(y_test, predictions):
    df = pd.DataFrame({'Actual': y_test.values, 'Predicted': predictions}, index=y_test.index)
    plt.figure(figsize=(12,6))
    sns.lineplot(data=df)
    plt.title("Actual vs Predicted Stock Prices")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.grid(True)
    return df

