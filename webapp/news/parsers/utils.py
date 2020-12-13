import requests

from fake_useragent import UserAgent
from webapp.db import db
from webapp.news.models import News


def get_html(url):
    ua = UserAgent()
    headers = {'User-Agent': ua.random}
    try:
        result = requests.get(url, headers=headers)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        return False


def save_news(title, url, published):
    news_exists = News.query.filter(News.url == url).count()
    if not news_exists:
        news_news = News(title=title, url=url, published=published)
        db.session.add(news_news)
        db.session.commit()        