from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        "author": "Sanjay R B",
        "title": "Blog Post 1",
        "content": "First Post Content",
        "date_posted": "Aug 20, 2020",
    },
    {
        "author": "Shari R B",
        "title": "Blog Post 2",
        "content": "Second Post Content",
        "date_posted": "Aug 19, 2020",
    },
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts, title="Data1")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
