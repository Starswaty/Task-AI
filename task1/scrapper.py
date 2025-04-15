import requests
from bs4 import BeautifulSoup

def fetch_top_news(limit=10):
    rss_url = "https://economictimes.indiatimes.com/rssfeeds/13357270.cms"
    news = []

    try:
        response = requests.get(rss_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'xml')
            items = soup.find_all('item')[:limit]
            for item in items:
                title = item.title.text
                link = item.link.text
                news.append({
                    'title': title,
                    'link': link
                })
        else:
            print(f"Failed to fetch feed. Status code: {response.status_code}")
    except Exception as e:
        print("Error occurred while fetching news:", e)

    return news
