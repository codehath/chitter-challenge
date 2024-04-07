import os
from peewee import *
from flask import Flask, request, render_template, redirect
from lib.person import *
from lib.peep import *

from datetime import datetime

# Create a new Flask app
app = Flask(__name__)

# Define your Peewee database instance
db = PostgresqlDatabase(
    'chitter-challenge',  # Your database name
    user='farhath',  # Your PostgreSQL username
    password='',  # Your PostgreSQL password
    host='localhost'  # Your PostgreSQL host
)

# Connect to the database
db.connect()


if db.table_exists(Person):
    # If the table exists, drop it
    db.drop_tables([Person])

db.create_tables([Person])

# new_user = Person(name='barry', username = 'bbop', email='barry@example.com', password='password', logged_in=False)
# new_user.save()

Person.create(
    name='John Doe',
    username='user',
    email='john@example.com',
    password='pass',
    logged_in=False
)

Person.create(
    name='Barry Allen',
    username='flash_speedster',
    email='barry.allen@example.com',
    password='SuperSecretPassword123',
    logged_in=False
)

Person.create(
    name='Diana Prince',
    username='wonder_woman',
    email='diana.prince@example.com',
    password='AmazingAmazon123',
    logged_in=False
)

Person.create(
    name='Clark Kent',
    username='superman',
    email='clark.kent@example.com',
    password='KryptoniteSucks456',
    logged_in=False
)

Person.create(
    name='Bruce Wayne',
    username='batman',
    email='bruce.wayne@example.com',
    password='IAmTheNight789',
    logged_in=False
)

# Person.create(name='John Doe', age=30)

if db.table_exists(Peep):
    # If the table exists, drop it
    db.drop_tables([Peep])

db.create_tables([Peep])
Peep.create(content='First Peep!', user_id=1)
Peep.create(content='Second Peep!', user_id=1)
Peep.create(content='Hello, Twitter!', user_id=2)
Peep.create(content='Python is awesome!', user_id=3)
Peep.create(content='Coding all day!', user_id=4)
Peep.create(content='Just had a great meal!', user_id=1)
Peep.create(content='Learning new technologies.', user_id=2)
Peep.create(content='Excited for the weekend!', user_id=3)
Peep.create(content='Reading a good book.', user_id=4)
Peep.create(content='Traveling to new places.', user_id=1)

# == Your Routes Here ==
# Pages
# HTML pages: register, login
# Templates: index, home

logged_in_user = None

## RENDER PAGES
@app.route('/', methods=['GET'])
def get_index():
    peeps = Peep.select()
    return render_template('index.html', peeps = peeps)

@app.route('/home', methods=['GET'])
def get_home():
    global logged_in_user
    if logged_in_user == None:
        return redirect("/login")
    peeps = Peep.select()
    return render_template('home.html', peeps = peeps, user = logged_in_user)

@app.route('/login', methods=['GET'])
def get_login():
    return render_template('/login.html')

@app.route('/register', methods=['GET'])
def get_register():
    return render_template('/register.html')

### POST REQUESTS
@app.route('/login', methods=['POST'])
def login():
    global logged_in_user
    username  = request.form['username']
    password  = request.form['password']
    
    if Person.select().where(Person.username == username).count() != 0:
        person = Person.select().where(Person.username == username).get()
        if person.password == password:
            person.logged_in = True
            person.save()
            logged_in_user = person
            return redirect("/home")
        else:
            message = "Invalid password"
    else:
        message = "Invalid username"
    return render_template('/login.html', message=message)

@app.route('/register', methods=['POST'])
def create_user():
    new_user = Person.create(name = request.form['name'], username = request.form['username'], email = request.form['email'], password = request.form['password'])
    return redirect("/home")

@app.route('/home', methods=['POST'])
def create_peep():
    global logged_in_user
    Peep.create(content = request.form['content'], user_id = logged_in_user.id)
    peeps = Peep.select()
    return render_template('home.html', peeps = peeps, user = logged_in_user)

### LOG OUT
@app.route('/home', methods=['DELETE'])
def log_out():
    global logged_in_user
    # return logged_in_user.username
    logged_in_user.logged_in = False
    logged_in_user.save()
    logged_in_user = None
    return redirect("/home")



# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':

    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
