from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def root():
    print("hello")
    return render_template("index.html")


@app.route('/login', methods=["POST"])
def login():
    print(request.form)
    return f"<h1>Name: {request.form['name']}, Password: {request.form['password']}</h1>"


if __name__ == "__main__":
    app.run(debug=True)
