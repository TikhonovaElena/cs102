from bottle import (
    route, run, template, request, redirect
)

import bottle
import string
import os
from scraputils import get_news
from db import News, session
from bayes import NaiveBayesClassifier


@route("/news")
def news_list():
    s = session()
    rows = s.query(News).filter(News.label == None).all()
    return template('news_template', rows=rows)


@route("/add_label/")
def add_label():
    s = session()
    news = s.query(News).filter(News.id == request.query.id).one()
    news.label = request.query.label
    s.commit()
    redirect("/news")


@route("/update")
def update_news():
    s = session()
    news_list = get_news("https://news.ycombinator.com/newest", n_pages=5)
    news_list_db = s.query(News).all()
    for new_news in news_list:
        is_in_the_db = False
        for old_news_db in news_list_db:
            if new_news["author"] == old_news_db.author and new_news["title"] == old_news_db.title:
                is_in_the_db = True
                break
        if not is_in_the_db:
            s.add(News(**new_news))
    s.commit()
    redirect("/news")


@route("/model")
def create_model():
    s = session()
    labeled_news = s.query(News).filter(News.label != None).all()
    x_train = [clean(news.title) for news in labeled_news]
    y_train = [news.label for news in labeled_news]
    classifier = NaiveBayesClassifier(0.05)
    [labels, model] = classifier.fit(x_train, y_train)
    return template("news_model", labels=labels, model=model )


@route("/classify")
def classify_news():
    s = session()
    labeled_news = s.query(News).filter(News.label != None).all()
    x_train = [clean(news.title) for news in labeled_news]
    y_train = [news.label for news in labeled_news]
    classifier = NaiveBayesClassifier(0.05)
    classifier.fit(x_train, y_train)
    rows = s.query(News).filter(News.label == None).all()
    good, maybe, never = [], [], []
    for row in rows:
        prediction = classifier.predict(clean(row.title))
        if prediction == "good":
            good.append(row)
        elif prediction == "maybe":
            maybe.append(row)
        else:
            never.append(row)
    return template("news_recommendations", good=good, maybe=maybe, never=never)


def clean(s):
    translator = str.maketrans("", "", string.punctuation)
    print(s.translate(translator).lower)
    return s.translate(translator).lower()


if __name__ == "__main__":
    path = os.path.dirname(os.path.realpath(__file__))
    views_path = os.path.join(path, "templates")
    bottle.TEMPLATE_PATH.insert(0, views_path)
    run(host="localhost", port=8080)

