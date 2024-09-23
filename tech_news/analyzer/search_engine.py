from ..database import search_news
from datetime import datetime


# Requisito 7
def search_by_title(title):
    ret = []
    for news in search_news({"title": {"$regex": title, "$options": "i"}}):
        ret.append((news['title'], news['url']))
    return ret


# Requisito 8
def search_by_date(date):
    try:
        date = datetime.strptime(date, "%Y-%m-%d")
        date = date.strftime("%d/%m/%Y")
    except ValueError:
        raise ValueError("Data inválida")
    ret = []
    for news in search_news({"timestamp": date}):
        ret.append((news['title'], news['url']))
    return ret


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    raise NotImplementedError
