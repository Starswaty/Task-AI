import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")
API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def trim_text(text, word_limit=800):
    """
    Trim the input text to a word count limit (approx. 512–1024 tokens).
    """
    words = text.split()
    return ' '.join(words[:word_limit]) if len(words) > word_limit else text

def generate_summary(text, max_length=130, min_length=30):
    """
    Generate summary using Hugging Face API with built-in trimming.
    """
    trimmed_text = trim_text(text)

    payload = {
        "inputs": trimmed_text,
        "parameters": {
            "max_length": max_length,
            "min_length": min_length,
            "do_sample": False
        }
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()
        summary = response.json()[0]["summary_text"]
        return summary
    except Exception as e:
        print(f"Error during summarization: {e}")
        print("Full response:", response.text)
        return "Summary generation failed."
