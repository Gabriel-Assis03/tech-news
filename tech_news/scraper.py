import requests
import time
# from bs4 import BeautifulSoup
from parsel import Selector

headers = {"user-agent": "Fake user-agent"}


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
    return Selector(html_content).css('h2.entry-title a::attr(href)').getall()
    # urlList = []
    # selector = Selector(html_content)
    # for newsUrl in selector.css('h2.entry-title a::attr(href)').getall():
    #     urlList.append(newsUrl)
    # return urlList


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
