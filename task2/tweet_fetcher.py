import tweepy
import os
from dotenv import load_dotenv

load_dotenv()
BEARER_TOKEN = os.getenv("BEARER_TOKEN")

client = tweepy.Client(bearer_token=BEARER_TOKEN)

def fetch_tweets(user, keyword, max_results=50):
    query = f'from:{user} "{keyword}" -is:retweet lang:en'
    try:
        tweets = client.search_recent_tweets(query=query,
                                             max_results=max_results,
                                             tweet_fields=["created_at", "text"])
        return tweets.data if tweets and tweets.data else []
    except Exception as e:
        print(f"Error fetching tweets for {user} with keyword '{keyword}':", e)
        return []
