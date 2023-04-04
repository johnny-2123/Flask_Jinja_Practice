# !!START
from flask import (Flask, render_template, redirect)
from .config import Config
from .tweets import tweets
from .form.form import Tweet
from datetime import date
import random

app = Flask(__name__)

app.config.from_object(Config)
# !!END


@app.route('/')
def hello():
    tweet = random.choice(list(tweets))
    return render_template('index.html', tweet=tweet)


@app.route('/feed')
def feed():
    return render_template('feed.html', tweets=tweets)


@app.route('/new', methods=['GET', "POST"])
def new_tweet():
    form = Tweet()
    if form.validate_on_submit():
        today = date.today()
        newdate = today.strftime("%d/%m/%Y")
        new_tweet = {
            'id': len(tweets),
            'author': form.data['author'],
            'tweet': form.data['tweet'],
            'date': newdate,
            'likes': 0
        }
        print(new_tweet)
        tweets.append(new_tweet)

        return redirect("/feed")
    if form.errors:
        return form.errors

    return render_template('new_tweet.html', form=form)


# @app.route("/new", methods=["GET", "POST"])
# def add_joke():
#     form = NewJokeFrom()

#     return render_template("joke_form.html", form=form)
