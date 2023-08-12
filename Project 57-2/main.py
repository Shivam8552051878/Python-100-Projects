from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
    url = "https://api.npoint.io/c790b4d5cab58020d391"
    all_post = requests.get(url).json()
    return render_template("index.html", post=all_post)


@app.route('/post/<int:index>')
def get_post(index):
    url = "https://api.npoint.io/c790b4d5cab58020d391"
    all_post = requests.get(url).json()
    return render_template("post.html", posts=all_post, id=index)


if __name__ == "__main__":
    app.run(debug=True)
