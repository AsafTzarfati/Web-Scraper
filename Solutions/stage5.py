import requests
import string
from bs4 import BeautifulSoup
import os

BASE_PAGE = 1
ERR_MSG = 'The URL returned '
WEB_BASE = "https://www.nature.com"
URL = "https://www.nature.com/nature/articles?sort=PubDate&year=2020"


def get_articles_by_type(all_articles, type_of_article):
    articles_by_type = list()
    for article in all_articles:
        article_type = "".join(article.find("span", {"class": "c-meta__type"}).contents)
        if article_type == type_of_article:
            articles_by_type.append(
                article.find("div", {"class": "c-card__body u-display-flex u-flex-direction-column"}))
    return articles_by_type


def scrap_article(article, path):
    article_dir = article.find("a").get("href")
    article_name = "".join(article.find("a", {"data-track-label": "link"}).contents)
    file_name = article_name.translate(str.maketrans("", "", string.punctuation)).replace(" ", "_")
    file = open(f"{path}/{file_name}.txt", "wb")
    r = requests.get(WEB_BASE + article_dir)
    if r.status_code == 200:
        soup = BeautifulSoup(r.content, "html.parser")
        my_text = soup.find("div", {"c-article-body u-clearfix"}).text.strip()
        file.write(my_text.encode())
        file.close()


def main():
    num_of_pages = int(input("Enter number of pages: "))
    type_of_article = input("Enter type of articles: ")
    for page_num in range(BASE_PAGE, num_of_pages + BASE_PAGE):
        pages = {"page": page_num}
        r = requests.get(URL, params=pages)
        if r.status_code == 200:
            soup = BeautifulSoup(r.content, "html.parser")
            all_articles = soup.findAll("article")
            if not os.access(f"Page_{page_num}", os.F_OK):
                try:
                    os.mkdir(f"Page_{page_num}")
                except FileExistsError:
                    print(f"Can't create a directory Page_{page_num}")
                    return
            for article in get_articles_by_type(all_articles, type_of_article):
                scrap_article(article, f"Page_{page_num}")
        else:
            print(ERR_MSG + str(r.status_code))


if __name__ == '__main__':
    main()
