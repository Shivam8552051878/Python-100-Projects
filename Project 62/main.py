from flask import Flask, render_template, request, redirect, url_for

import sqlite3

db = sqlite3.connect("book-collection.db", check_same_thread=False)
cursor = db.cursor()
# cursor.execute('CREATE TABLE books '
#                '(id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, '
#                'author varchar(250) NOT NULL, rating FLOAT NOT NULL)')


app = Flask(__name__)

# all_books = [
#     {
#         "title": "Harry Potter",
#         "author": "J. K. Rowling",
#         "rating": 9,
#     }
# ]


@app.route('/')
def home():
    all_books = cursor.execute("SELECT * FROM books").fetchall()
    db.commit()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        # request.form.get("name")
        cursor.execute("INSERT INTO books (title,author,rating) VALUES(?,?,?)",
                       (str(request.form.get('name')), str(request.form.get('author')),
                        float(request.form.get('rating'))))
        db.commit()

        redirect(url_for('add'))
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)
