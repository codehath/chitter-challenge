from peewee import *
from datetime import datetime

db = PostgresqlDatabase('chitter-challenge', user='farhath', password='', host='localhost')

class Peep(Model):
    id = AutoField()
    content = CharField()
    timestamp =  DateTimeField(default=datetime.now())
    user_id = IntegerField() # Foreign key to person table
    
    class Meta:
        database = db