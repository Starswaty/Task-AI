import feedparser
import pandas as pd

def fetch_tech_news():
    sources = {
        "Economic Times": "https://economictimes.indiatimes.com/tech/rssfeeds/13357270.cms",
        "Business Standard": "https://www.business-standard.com/rss/technology-106.rss",
        "Moneycontrol": "https://www.moneycontrol.com/rss/technology.xml"
    }

    all_news = []
    for source, url in sources.items():
        feed = feedparser.parse(url)
        for entry in feed.entries[:10]:
            all_news.append({
                'Title': entry.title,
                'Link': entry.link,
                'Published': entry.published,
                'Source': source
            })

    df = pd.DataFrame(all_news)
    df.to_csv("news.csv", index=False)
    return df

