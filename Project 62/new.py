from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import sqlite3

db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///book-collection.db"
db.init_app(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String)


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    users = db.session.execute(db.select(Books).order_by(Books.id)).scalars().fetchall()
    # print(type(users[0].username), users[0].username)
    return render_template("index.html", books=users)




@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        book = Books(
            title=request.form["name"],
            author=request.form["author"],
            rating=request.form["rating"]
        )
        db.session.add(book)
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("add.html")


# @app.route('/')
# def home():
#     users = db.session.execute(db.select(User).order_by(User.username)).scalars().fetchall()
#     print(type(users[0].username), users[0].username)
#     return render_template("index.html", books=users)
#
#
#
#
# @app.route("/add", methods=["GET", "POST"])
# def add():
#     if request.method == "POST":
#         user = User(
#             username=request.form["name"],
#             email=request.form["author"],
#         )
#         db.session.add(user)
#         db.session.commit()
#         return redirect(url_for("home"))
#
#     return render_template("add.html")


# @app.route("/user/<int:id>")
# def user_detail(id):
#     user = db.get_or_404(User, id)
#     return render_template("user/detail.html", user=user)
#
#
# @app.route("/user/<int:id>/delete", methods=["GET", "POST"])
# def user_delete(id):
#     user = db.get_or_404(User, id)
#
#     if request.method == "POST":
#         db.session.delete(user)
#         db.session.commit()
#         return redirect(url_for("user_list"))
#
#     return render_template("user/delete.html", user=user)


if __name__ == "__main__":
    app.run(debug=True)
