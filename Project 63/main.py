from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from myform import MyForm, UpdateForm
import requests

db = SQLAlchemy()

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movie-collection.db"
db.init_app(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    date = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    review = db.Column(db.String, nullable=False)
    overview = db.Column(db.String, nullable=False)
    ranking = db.Column(db.Float, nullable=False)
    img_url = db.Column(db.String, nullable=False)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    # movies = db.session.execute(db.select(Movie).order_by(Movie.rating)).scalars().fetchall()
    # This line creates a list of all the movies sorted by rating
    all_movies = Movie.query.order_by(Movie.rating).all()
    print(all_movies[0].title)

    # This line loops through all the movies
    for i in range(len(all_movies)):
        # This line gives each movie a new ranking reversed from their order in all_movies
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", all_movie=all_movies)


@app.route("/update/<int:index>", methods=["GET", "POST"])
def update(index):
    form = UpdateForm()
    movie_title = db.session.execute(db.select(Movie).where(Movie.id == index)).scalar().title
    movie_to_update = db.session.execute(db.select(Movie).where(Movie.id == index)).scalar()

    # print(movie_title.rating)
    # print(movie_title)
    if form.validate_on_submit():
        # print(movie_to_update)
        movie_to_update.rating = float(form.rating.data)
        movie_to_update.review = form.review.data
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("edit.html", form=form, title=movie_title)


@app.route("/delete")
def delete():
    movie_id = request.args.get("index")
    movie = Movie.query.get(movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/add", methods=["GET", "POST"])
def add():
    form = MyForm()
    if form.validate_on_submit():
        # print(form.title.data)
        movie = Movie(title=form.title.data, date=form.date.data, rating=form.rating.data, review=form.review.data
                      , overview=form.overview.data, ranking=form.ranking.data, img_url=form.img_url.data)
        # print(movie.img_url)
        db.session.add(movie)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("add.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
