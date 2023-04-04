from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class Tweet(FlaskForm):
    author = StringField('author', validators=[DataRequired()])
    tweet = StringField('tweet', validators=[DataRequired()])
    submit = SubmitField("Create Tweet")
