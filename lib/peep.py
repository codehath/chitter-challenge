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


class Peep(Model):
    id = AutoField()
    content = CharField()
    timestamp = DateTimeField(default=datetime.now())
    user_id = IntegerField()  # Foreign key to person table

    class Meta:
        database = db
