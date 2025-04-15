import requests
from bs4 import BeautifulSoup

def scrape_et_tech_rss():
    url = 'https://economictimes.indiatimes.com/tech/rssfeeds/13357270.cms'
    try:
        res = requests.get(url)
        res.raise_for_status()
        soup = BeautifulSoup(res.content, 'xml')

        articles = []
        for item in soup.find_all('item'):
            title = item.title.text.strip()
            link = item.link.text.strip()
            if title and link:
                articles.append({
                    "title": title,
                    "source": "Economic Times",
                    "link": link
                })
        return articles

    except Exception as e:
        print("Error fetching Economic Times:", e)
        return []

def scrape_moneycontrol():
    url = 'https://www.moneycontrol.com/news/business/'
    try:
        soup = BeautifulSoup(requests.get(url).text, 'html.parser')
        articles = []
        for a in soup.select('li.clearfix a'):
            title = a.text.strip()
            link = a.get('href', '').strip()
            if title and link and link.startswith('http'):
                articles.append({
                    "title": title,
                    "source": "Moneycontrol",
                    "link": link
                })
        return articles
    except Exception as e:
        print("Error fetching Moneycontrol:", e)
        return []

def scrape_business_standard():
    url = 'https://www.business-standard.com/category/technology/news'
    try:
        soup = BeautifulSoup(requests.get(url).text, 'html.parser')
        articles = []
        for a in soup.select('h2 a'):
            title = a.text.strip()
            href = a.get('href', '').strip()
            if title and href:
                link = 'https://www.business-standard.com' + href
                articles.append({
                    "title": title,
                    "source": "Business Standard",
                    "link": link
                })
        return articles
    except Exception as e:
        print("Error fetching Business Standard:", e)
        return []

def scrape_cnbc_tv18():
    url = 'https://www.cnbctv18.com/technology/'
    try:
        soup = BeautifulSoup(requests.get(url).text, 'html.parser')
        articles = []
        for a in soup.select('a.headline'):
            title = a.text.strip()
            href = a.get('href', '').strip()
            if title and href:
                link = 'https://www.cnbctv18.com' + href
                articles.append({
                    "title": title,
                    "source": "CNBC TV18",
                    "link": link
                })
        return articles
    except Exception as e:
        print("Error fetching CNBC TV18:", e)
        return []

def scrape_livemint():
    url = 'https://www.livemint.com/technology'
    try:
        soup = BeautifulSoup(requests.get(url).text, 'html.parser')
        articles = []
        for a in soup.select('a.headline'):
            title = a.text.strip()
            href = a.get('href', '').strip()
            if title and href:
                link = 'https://www.livemint.com' + href
                articles.append({
                    "title": title,
                    "source": "LiveMint",
                    "link": link
                })
        return articles
    except Exception as e:
        print("Error fetching LiveMint:", e)
        return []
