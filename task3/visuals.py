import pandas as pd
import plotly.graph_objects as go
import streamlit as st  

def get_percent_change(dataframe: pd.DataFrame) -> pd.DataFrame:
    dataframe['% Change'] = dataframe['Close'].pct_change() * 100
    return dataframe

def draw_comparison_chart(exchange_df: pd.DataFrame, stock_df: pd.DataFrame, title="Currency vs Stock Movement"):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=exchange_df.index, y=exchange_df['% Change'], mode='lines', name='FX Movement'))
    fig.add_trace(go.Scatter(x=stock_df.index, y=stock_df['% Change'], mode='lines', name='Stock Movement'))
    
    fig.update_layout(
        title=title,
        xaxis_title="Date",
        yaxis_title="Daily % Change",
        template="plotly_dark"
    )
    
    st.plotly_chart(fig, use_container_width=True)  

def send_alert(message, receiver="your_email@example.com"):
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart

    sender = "your_email@example.com"
    password = "your_password"

    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = 'Currency Impact Notification'
    msg.attach(MIMEText(message, 'plain'))

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())