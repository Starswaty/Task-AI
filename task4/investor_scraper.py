import requests
from bs4 import BeautifulSoup

def scrape_infosys_investor():
    url = 'https://www.infosys.com/investors/reports-filings/'
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    reports = []
    for item in soup.select('ul li a'):
        title = item.text.strip()
        link = 'https://www.infosys.com' + item.get('href', '')
        reports.append({"title": title, "link": link, "source": "Infosys"})
    return reports

def scrape_tcs_investor():
    url = 'https://www.tcs.com/investor-relations'
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    reports = []
    for item in soup.select('a[href*="pdf"]'):
        title = item.text.strip()
        link = 'https://www.tcs.com' + item.get('href', '')
        reports.append({"title": title, "link": link, "source": "TCS"})
    return reports

def scrape_wipro_investor():
    url = 'https://www.wipro.com/investors/annual-reports/'
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    reports = []
    for item in soup.select('a[href$=".pdf"]'):
        title = item.text.strip()
        link = item.get('href', '')
        reports.append({"title": title, "link": link, "source": "Wipro"})
    return reports

def scrape_hcl_investor():
    url = 'https://www.hcltech.com/investors/financial-reports'
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    reports = []
    for item in soup.select('a[href$=".pdf"]'):
        title = item.text.strip()
        link = item.get('href', '')
        reports.append({"title": title, "link": link, "source": "HCL"})
    return reports

def scrape_techm_investor():
    url = 'https://www.techmahindra.com/investors/financials/'
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    reports = []
    for item in soup.select('a[href$=".pdf"]'):
        title = item.text.strip()
        link = item.get('href', '')
        reports.append({"title": title, "link": link, "source": "Tech Mahindra"})
    return reports
