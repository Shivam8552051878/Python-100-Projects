import datetime
import random

import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(0, 100)
    data = datetime.datetime.today().year
    # response = requests.get("https://api.agify.io/?name=shivam")

    return render_template("index.html", num=random_number, yu=data)


@app.route('/<name>')
def challange(name):
    gender_url = "https://api.genderize.io"
    param = {
        "name": name
    }
    response = requests.get(gender_url, params=param)
    gender = response.json()["gender"]

    age_url = "https://api.agify.io"
    age_response = requests.get(age_url, params=param)
    age_response.raise_for_status()
    age = age_response.json()["age"]

    if age == None or gender == None:
        return "Sorry wrong input"
    else:
        return render_template("chall.html", user={"name": name, "gender": gender, "age": age})


@app.route('/blog')
def get_blog():
    url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url)
    all_post = response.json()
    return render_template("blog.html", post=all_post)


if __name__ == "__main__":
    app.run(debug=True)
