from flask import Flask
app = Flask(__name__)


def make_bold(function):
    def inner_func():
        return "<b>"+function()+"</b>"
    return inner_func


def make_em(function):
    def inner_func():
        return "<em>"+function()+"</em>"
    return inner_func

def make_und(function):
    def inner_func():
        return "<u>"+function()+"</u>"
    return inner_func

@app.route('/')
def hello_world():
    return "<p>Hello World!</p>"


@app.route("/bye")
@make_bold
@make_em
@make_und
def bye():
    return "Bye!"


if __name__ == "__main__":
    app.run(debug=True)
