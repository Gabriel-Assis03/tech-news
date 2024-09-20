import requests
from bs4 import BeautifulSoup
import time

headers = { "user-agent": "Fake user-agent" }

# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        page = requests.get(url, timeout=3)
    except requests.ReadTimeout:
        return None
    if page.status_code == 200:
        html_page = page.text
        return html_page
    else:
        return None


# Requisito 2
def scrape_updates(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    raise NotImplementedError
