from ..database import search_news
from datetime import datetime


def format_return(data):
    # ret = []
    # for news in data:
    #     ret.append((news['title'], news['url']))
    # return ret
    return [(news['title'], news['url']) for news in data]


# Requisito 7
def search_by_title(title):
    data = search_news({"title": {"$regex": title, "$options": "i"}})
    return format_return(data)


# Requisito 8
def search_by_date(date):
    try:
        date = datetime.strptime(date, "%Y-%m-%d")
        date = date.strftime("%d/%m/%Y")
    except ValueError:
        raise ValueError("Data inválida")
    return format_return(search_news({"timestamp": date}))


# Requisito 9
def search_by_category(category):
    data = search_news({"category": {"$regex": category, "$options": "i"}})
    return format_return(data)
