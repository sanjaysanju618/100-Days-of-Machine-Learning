from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config["SECRET_KEY"] = "c4f6d6ef332784d4411e5df87bedc385"

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


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", category="success")
        return redirect(url_for("home"))
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "sanjay@gmail.com" and form.password.data == "password":
            flash("You are logged in!", category="success")
            return redirect(url_for("home"))
        else:
            flash("Login Unsuccess!", category="danger")
    return render_template("login.html", title="Login", form=form)


if __name__ == "__main__":
    app.run(debug=True)
