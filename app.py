from peewee import *
from flask import Flask, request, render_template, redirect, session
from lib.env_variables import *
from lib.person import *
from lib.peep import *
import os
import bcrypt


from datetime import datetime

# Create a new Flask app
app = Flask(__name__)

# Set a secret key for session encryption
app.secret_key = os.environ.get("SECRET_KEY", "your_secret_key_here")

db = PostgresqlDatabase(db_name, user=db_user, password=db_password, host=db_host)

# Connect to the database
db.connect()
db.create_tables([Person, Peep], safe=True)


# == Your Routes Here ==
# Pages
# HTML pages: register, login
# Templates: index, home

logged_in_user = None


## RENDER PAGES
@app.route("/", methods=["GET"])
def get_index():
    peeps = Peep.select()
    return render_template("index.html", peeps=peeps)


@app.route("/home", methods=["GET"])
def get_home():
    if "user_id" not in session:  # Redirect to login if user is not authenticated
        return redirect("/login")

    user_id = session["user_id"]
    logged_in_user = Person.get_by_id(user_id)
    peeps = Peep.select()
    return render_template("home.html", peeps=peeps, user=logged_in_user)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        username = request.form["username"]
        password = request.form["password"].encode("utf-8")

        try:
            person = Person.select().where(Person.username == username).get()
        except Person.DoesNotExist:
            message = "Invalid username"
            return render_template("login.html", message=message)

        if bcrypt.checkpw(password, person.password.encode("utf-8")):
            session["user_id"] = (
                person.id
            )  # Set user_id in session upon successful login
            return redirect("/home")
        else:
            message = "Invalid password"
            return render_template("login.html", message=message)


@app.route("/register", methods=["GET"])
def get_register():
    return render_template("/register.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        password = request.form["password"].encode("utf-8")
        hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())

        person = Person.create(
            name=request.form["name"],
            username=request.form["username"],
            email=request.form["email"],
            password=hashed_password.decode("utf-8"),
        )
        session["user_id"] = (
            person.id
        )  # Set user_id in session upon successful registration
        return redirect("/home")


@app.route("/logout", methods=["GET"])
def logout():
    session.pop("user_id", None)  # Remove user_id from session upon logout
    return redirect("/")


@app.route("/home", methods=["POST"])
def create_peep():
    if "user_id" not in session:  # Redirect to login if user is not authenticated
        return redirect("/login")

    user_id = session["user_id"]
    Peep.create(content=request.form["content"], user_id=user_id)
    peeps = Peep.select()
    return render_template("home.html", peeps=peeps, user=Person.get_by_id(user_id))


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == "__main__":

    app.run(debug=True, port=int(os.environ.get("PORT", 5001)))
