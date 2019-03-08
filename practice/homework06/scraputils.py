import requests
from bs4 import BeautifulSoup


def extract_news(parser):
    """ Extract news from a given web page """
    news_list = []
    news_table = parser.find_all("tr", {"class": "athing"})
    info = parser.find_all("td", {"class": "subtext"})
    for news_index in range(len(news_table)):
        comments = 0
        links = info[news_index].find_all("a")
        title = news_table[news_index].find(class_="storylink")
        points = info[news_index].span.text.split()[0]
        if links[-1].text != "discuss":
            comments = int(links[-1].text.split()[0])
        news = {
            "author": links[0].text,
            "comments": comments,
            "points": points,
            "title": title.text,
            "url": title["href"],
            "label": None
        }
        news_list.append(news)
    return news_list


def extract_next_page(parser):
    """ Extract next page URL """
    return parser.table.find_all("table")[1].find_all("a")[-1]["href"]


def get_news(url, n_pages=1):
    """ Collect news from a given web page """
    news = []
    while n_pages:
        print("Collecting data from page: {}".format(url))
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        news_list = extract_news(soup)
        next_page = extract_next_page(soup)
        url = "https://news.ycombinator.com/" + next_page
        news.extend(news_list)
        n_pages -= 1
    return news

