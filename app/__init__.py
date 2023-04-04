# !!START
from flask import (Flask, render_template)
from .config import Config
from .tweets import tweets
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
