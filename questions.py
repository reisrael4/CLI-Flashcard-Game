from peewee import *

db = PostgresqlDatabase('questions', user='postgres', password='', host='localhost', port=5432)

class BaseModel(Model):
    class Meta:
        database = db

class Question(BaseModel):
    question: CharField()
    answer_a: CharField()
    answer_b: CharField()
    answer_c: CharField()
    correct_answer: CharField()

db.connect()
db.drop_tables([Question])
db.create_tables([Question])

question_1 = Question(question="Which of these is a vehicle with three wheels?", answer_a="A Tricycle", answer_b= "B Trick Daddy", answer_c= "C Triceratops", correct_answer= "A")
question_1.save()
question_2 = Question(question="What word does Aretha Franklin spell out in her iconic 1967 hit?", answer_a="A Respect", answer_b= "B Robocop", answer_c= "C Ridonkulous", correct_answer= "A")
question_2.save()