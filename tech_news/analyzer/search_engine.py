from ..database import search_news


# Requisito 7
def search_by_title(title):
    data = search_news({"title": {"$regex": title, "$options": "i"}})
    ret = []
    for news in data:
        ret.append((news['title'], news['url']))
    return ret


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    raise NotImplementedError
