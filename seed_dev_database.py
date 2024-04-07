from lib.person import *
from lib.peep import *
from dotenv import load_dotenv
import os
import bcrypt

# Load environment variables from .env file
load_dotenv()

# Get database configuration from environment variables or use default values
db_name = os.environ.get("DB_NAME", "default_db_name")
db_user = os.environ.get("DB_USER", "default_user")
db_password = os.environ.get("DB_PASSWORD", "")
db_host = os.environ.get("DB_HOST", "localhost")

# Create a PostgresqlDatabase instance using the configuration
db = PostgresqlDatabase(db_name, user=db_user, password=db_password, host=db_host)

# Connect to the database
db.connect()


# Function to hash a password
def hash_password(password):
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


# Flush existing data
db.drop_tables([Person, Peep])
db.create_tables([Person, Peep])

# Seed data for Person
persons = [
    {
        "name": "John Doe",
        "username": "user",
        "email": "john@example.com",
        "password": "pass",
    },
    {
        "name": "Barry Allen",
        "username": "flash_speedster",
        "email": "barry.allen@example.com",
        "password": "SuperSecretPassword123",
    },
    {
        "name": "Diana Prince",
        "username": "wonder_woman",
        "email": "diana.prince@example.com",
        "password": "AmazingAmazon123",
    },
    {
        "name": "Clark Kent",
        "username": "superman",
        "email": "clark.kent@example.com",
        "password": "KryptoniteSucks456",
    },
    {
        "name": "Bruce Wayne",
        "username": "batman",
        "email": "bruce.wayne@example.com",
        "password": "IAmTheNight789",
    },
]

# Seed data for Peep
peeps = [
    {"content": "First Peep!", "user_id": 1},
    {"content": "Second Peep!", "user_id": 1},
    {"content": "Hello, Twitter!", "user_id": 2},
    {"content": "Python is awesome!", "user_id": 3},
    {"content": "Coding all day!", "user_id": 4},
    {"content": "Just had a great meal!", "user_id": 1},
    {"content": "Learning new technologies.", "user_id": 2},
    {"content": "Excited for the weekend!", "user_id": 3},
    {"content": "Reading a good book.", "user_id": 4},
    {"content": "Traveling to new places.", "user_id": 1},
]

# Insert Person data
for person in persons:
    Person.create(
        name=person["name"],
        username=person["username"],
        email=person["email"],
        password=hash_password(person["password"]),  # Hash password before storing
        logged_in=False,
    )

# Insert Peep data
for peep in peeps:
    Peep.create(content=peep["content"], user_id=peep["user_id"])


print("Database seeding complete.")
