from peewee import *
from datetime import datetime
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get database configuration from environment variables or use default values
db_name = os.environ.get("DB_NAME", "default_db_name")
db_user = os.environ.get("DB_USER", "default_user")
db_password = os.environ.get("DB_PASSWORD", "")
db_host = os.environ.get("DB_HOST", "localhost")

# Create a PostgresqlDatabase instance using the configuration
db = PostgresqlDatabase(db_name, user=db_user, password=db_password, host=db_host)


class Person(Model):
    id = AutoField()
    name = CharField()
    username = CharField()
    email = CharField()
    password = CharField()
    logged_in = BooleanField(default=False)

    class Meta:
        database = db  # This model uses the "people.db" database.
