from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/bye')
@make_bold
def bye():
    return '<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRHc2UyQIQtezXgUX9KqINoQJ8wD4F8AnLaIES0KJ_3&s">' \
           'he'

@app.route('/<name>/<int:age>')
def hello(name, age):
    return f"Hello {name} your age is {age} !!"

if __name__ == "__main__":
    app.run(port=4444, debug=True)
