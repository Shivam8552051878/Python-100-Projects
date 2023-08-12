from flask import Flask
from random import randint

app = Flask(__name__)

NUM = randint(0,9)


def make_h1(function):
    def wrapper():
        return f'<h1><b>{function()}</b></h1>'
    return wrapper

@app.route("/")
@make_h1
def home():
    return f'Guess a number between 0 and 9 {NUM}' \
           '<br/>' \
           '<img src="https://i.giphy.com/3o7aCSPqXE5C6T8tBC.gif">'


@app.route("/<int:number>")
def higher_lower(number):
    if number == NUM:
        return 'You Found Me' \
           '<br/>' \
           '<img src="https://i.giphy.com/3o6ZtaO9BZHcOjmErm.gif">'
    elif number > NUM:
        return 'Its Two High' \
           '<br/>' \
           '<img src=https://media2.giphy.com/media/YLxD2fPjWPw6A/giphy.gif?cid=ecf05e47sy83kr4qp9dy281h0pm5yuvl19s4e2jur4yhp4d3&ep=v1_gifs_search&rid=giphy.gif&ct=g">'
    else:
        return 'Its Two Low' \
           '<br/>' \
           '<img src="https://media1.giphy.com/media/IevhwxTcTgNlaaim73/giphy.gif?cid=ecf05e47mahmj751rvcrjznvel66e2n24zawafpnph1fuspk&ep=v1_gifs_search&rid=giphy.gif&ct=g" >'



if __name__ == "__main__":
    app.run(debug=True)