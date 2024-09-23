import requests
import time
import re
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
    # selector = Selector(html_content)
    # nextUrl = selector.css('a.next.page-numbers::attr(href)').get()
    # return nextUrl
    return Selector(html_content).css('a.next.page-numbers::attr(href)').get()


# Requisito 4
def scrape_news(html_content):
    selector = Selector(html_content)
    newsUrl = selector.css('link[rel="canonical"]::attr(href)').get()
    newsTitle = selector.css('h1.entry-title::text').get()
    title = newsTitle.replace('\xa0', ' ').strip()
    newsDate = selector.css('li.meta-date::text').get()
    newsWriter = selector.css('span.author a.url.fn.n::text').get()
    strTime = selector.css('li.meta-reading-time::text').get()
    newsReadingTime = re.search(r'\d+', strTime)
    newsCategory = selector.css('span.label::text').get()
    summary = selector.css('div.entry-content p').xpath('string()').get()
    newsSummary = summary.replace('\xa0', ' ').strip()
    return {
        "url": newsUrl,
        "title": title,
        "timestamp": newsDate,
        "writer": newsWriter,
        "reading_time": int(newsReadingTime.group()),
        "summary": newsSummary,
        "category": newsCategory,
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    raise NotImplementedError
