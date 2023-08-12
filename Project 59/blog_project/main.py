import os

from flask import Flask, render_template, request
from data import PostData
import requests
import smtplib

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


# @app.route("/contact")
# def contact():
#     return render_template("contact.html")


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


# @app.route("/form-entery", methods=["POST"])
# def mail_it():
#     name = request.form['name'].title()
#     phone = request.form['phone']
#     email = request.form['email']
#     message = request.form['message']
#     with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#         connection.starttls()
#         connection.login(os.environ.get("EMAIL"), os.environ.get("PASSWORD"))
#         connection.sendmail(from_addr=os.environ.get("EMAIL"), to_addrs="sg9967780426@gmail.com",
#                             msg=f"Subject: Enquery from {name}\n\n Name: {name}\nContact No: {phone}\nEmail Id: {email}\nMesssage: {message}")
#         return "<h1>SuccessfUll Message Send</h1>"
#
#     return "Problem is sending message"


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(os.environ.get("EMAIL"), os.environ.get("PASSWORD"))
        connection.sendmail(os.environ.get("EMAIL"), os.environ.get("EMAIL"), email_message)
        print("MSg Send succesfully")


if __name__ == "__main__":
    app.run(debug=True)