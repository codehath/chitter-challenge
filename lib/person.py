from peewee import *

db = PostgresqlDatabase('chitter-challenge', user='farhath', password='', host='localhost')

class Person(Model):
    id = AutoField()
    name = CharField()
    username = CharField()
    email = CharField()
    password = CharField()
    logged_in = BooleanField(default=False)

    class Meta:
        database = db # This model uses the "people.db" database.