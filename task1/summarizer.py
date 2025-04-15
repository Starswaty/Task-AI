import requests
import os
from dotenv import load_dotenv


load_dotenv()

HUGGINGFACE_API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")

def summarize_article(text, min_length=80, max_length=130):
    if not text.strip():
        return "⚠️ No content to summarize."

    API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
    headers = {
        "Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "inputs": text,
        "parameters": {
            "min_length": min_length,
            "max_length": max_length,
            "do_sample": False
        }
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()
        summary = response.json()[0]['summary_text']
        return summary.strip()
    except requests.exceptions.RequestException as e:
        return f"⚠️ API request failed: {str(e)}"
    except Exception as e:
        return f"⚠️ Summarization failed: {str(e)}"
