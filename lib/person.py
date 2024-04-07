from peewee import *
from datetime import datetime
from lib.env_variables import *

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
