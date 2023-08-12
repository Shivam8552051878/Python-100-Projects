from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField
from wtforms.validators import DataRequired, URL


class MyForm(FlaskForm):
    title = StringField(label="Title", name="title", validators=[DataRequired()])
    date = StringField(label="Date EX:-2017", name="date", validators=[DataRequired()])
    rating = StringField(label="Rating", name="rating", validators=[DataRequired()])
    review = StringField(label="Review", name="review", validators=[DataRequired()])
    overview = StringField(label="Description", name="overview", validators=[DataRequired()])
    ranking = StringField(label="Ranking", name="ranking", validators=[DataRequired()])
    img_url = StringField(label="Image Url", name="url", validators=[DataRequired(), URL()])
    submit = SubmitField(label="submit")


class UpdateForm(FlaskForm):
    rating = StringField(label="Your Rating Out of 10 EX:7.5", name="rating", validators=[DataRequired()])
    review = StringField(label="Review", name="review", validators=[DataRequired()])
    submit = SubmitField(label="submit")

