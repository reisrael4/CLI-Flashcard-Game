from peewee import *

db = PostgresqlDatabase('questions', user='postgres', password='', host='localhost', port=5432)

class BaseModel(Model):
    class Meta:
        database = db

class Question(BaseModel):
    question: CharField()
    answers: 