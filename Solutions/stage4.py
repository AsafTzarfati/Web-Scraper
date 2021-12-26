import requests
import string
from bs4 import BeautifulSoup
ERR_MSG = 'The URL returned '
WEB_BASE = "https://www.nature.com"
URL = "https://www.nature.com/nature/articles?sort=PubDate&year=2020&page=3"


def get_news_article(all_articles):
    all_news_article = list()
    for article in all_articles:
        article_type = "".join(article.find("span", {"class": "c-meta__type"}).contents)
        if article_type == "News":
            all_news_article.append(
                article.find("div", {"class": "c-card__body u-display-flex u-flex-direction-column"}))
    return all_news_article


def scrap_news(article):
    article_dir = article.find("a").get("href")
    article_name = "".join(article.find("a", {"data-track-label": "link"}).contents)
    file_name = article_name.translate(str.maketrans('', '', string.punctuation)).replace(" ", "_")
    file = open(f"{file_name}.txt", "wb")
    r = requests.get(WEB_BASE + article_dir)
    if r.status_code == 200:
        soup = BeautifulSoup(r.content, 'html.parser')
        my_text = soup.find("div", {"c-article-body u-clearfix"}).text.strip()
        file.write(my_text.encode())
        file.close()


def main():
    r = requests.get(URL)
    if r.status_code == 200:
        soup = BeautifulSoup(r.content, 'html.parser')
        all_articles = soup.findAll("article")
        for news in get_news_article(all_articles):
            scrap_news(news)
    else:
        print(ERR_MSG + str(r.status_code))


if __name__ == '__main__':
    main()
