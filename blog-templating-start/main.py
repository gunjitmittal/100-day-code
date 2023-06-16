from flask import Flask, render_template
import requests
app = Flask(__name__)
blog_url = "https://api.npoint.io/1d79c312d6848f5e07ae"



@app.route('/')
def home():
    blogs = requests.get(blog_url).json()
    return render_template("index.html", blogs=blogs)


@app.route("/post/<int:blog_id>")
def get_blog(blog_id):
    blogs = requests.get(blog_url).json()
    return render_template("post.html", blog=blogs[blog_id-1])


if __name__ == "__main__":
    app.run(debug=True)
