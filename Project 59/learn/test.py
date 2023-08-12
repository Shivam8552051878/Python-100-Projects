from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    return f"Name: {request.form['username']} password: {request.form['password']}"


if __name__ == "__main__":
    app.run(debug=True)