from peewee import *
from datetime import datetime
from lib.env_variables import *

db = PostgresqlDatabase(db_name, user=db_user, password=db_password, host=db_host)


class Peep(Model):
    id = AutoField()
    content = CharField()
    timestamp = DateTimeField(default=datetime.now())
    user_id = IntegerField()  # Foreign key to person table

    class Meta:
        database = db
