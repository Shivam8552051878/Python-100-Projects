from flask import Flask, render_template
from data import PostData
import requests

app = Flask(__name__)
url = "https://api.npoint.io/7d3bf0036ca927e20c85"
data = []
response = requests.get(url=url)
for post in response.json():
    data.append(PostData(id=post["id"], body=post["body"], title=post["title"], subtitle=post["subtitle"], author=post["author"], image_url=post["image"], date=post["date"]))
@app.route("/")
def home():
    return render_template("index.html", posts=data)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post")
def post():
    return render_template("post.html",post=data[0])





@app.route("/post/<int:index>")
def show_post(index = 1):
    info = None
    for post in data:
        if post.id == index:
            info = post
    return render_template("post.html", post=info)


if __name__ == "__main__":
    app.run(debug=True)