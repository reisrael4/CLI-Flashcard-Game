from peewee import *

db = PostgresqlDatabase('questions', user='postgres', password='', host='localhost', port=5432)

class BaseModel(Model):
    class Meta:
        database = db

class Question(BaseModel):
    question= CharField()
    answer_a= CharField()
    answer_b= CharField()
    answer_c= CharField()
    correct_answer= CharField()
    card_count= IntegerField()


question_data = [{"question": "Which of these is a vehicle with three wheels?", 'answer_a':"A Tricycle", 'answer_b': "B Trick Daddy", 'answer_c': "C Triceratops", 'correct_answer': "A", "card_count": 0}, 
    {"question":"What word does Aretha Franklin spell out in her iconic 1967 hit?", 'answer_a':"A Respect", 'answer_b': "B Robocop", 'answer_c': "C Ridonkulous", 'correct_answer': "A", "card_count": 0},
    {"question":"What Canadian province's name is Latin for 'New Scotland'?", 'answer_a': "A Nova Scotia", 'answer_b': "B Ontario", 'answer_c': "C Alberta", 'correct_answer': "A", "card_count": 0},
    {"question":"Which of these speeds is typically fastest?", "answer_a":"A Speed of light", "answer_b":"B Speed of sound", "answer_c":"C They're the same", "correct_answer":"A", "card_count": 0},
    {"question":"Three consecutive strikes is known as a turkey in which of these sports?", "answer_a":"A Bowling", "answer_b":"B Cricket", "answer_c":"C Volleyball", "correct_answer":"A", "card_count": 0},
    {"question":"At the start of his career, Justin Bieber was mentored by which of these musicians?", "answer_a":"A Jay-Z", "answer_b":"B Usher", "answer_c":"C DJ Khaled", "correct_answer":"B", "card_count": 0},
    {"question":"By definition, which of these words can refer to a college graduation ceremony?", "answer_a":"A Initiation", "answer_b":"B Matriculation", "answer_c":"C Commencement", "correct_answer":"C", "card_count": 0},
    {"question":"Which of these baseball pitches puts the least spin on the ball?", "answer_a":"A Curveball", "answer_b":"B Knuckleball", "answer_c":"C Fastball", "correct_answer":"B", "card_count": 0},
    {"question":"The name of Shakespeare's only son is one letter off from the title of what play?", "answer_a":"A Macbeth", "answer_b":"B Hamlet", "answer_c":"C Othello", "correct_answer":"B", "card_count": 0},
    {"question":"Which of these terms comes from a French phrase that means 'come help me'?", "answer_a":"A SOS", "answer_b":"B Ahoy", "answer_c":"C Mayday", "correct_answer":"C", "card_count": 0},
]

db.connect()
db.drop_tables([Question])
db.create_tables([Question])

for list_element in question_data:
    list_element = Question(question = list_element['question'], answer_a = list_element['answer_a'], answer_b = list_element['answer_b'], answer_c = list_element['answer_c'], correct_answer = list_element['correct_answer'], card_count = 0)
    list_element.save()