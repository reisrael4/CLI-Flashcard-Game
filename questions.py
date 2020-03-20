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
    card_count= 0


question_data = [{"question": "Which of these is a vehicle with three wheels?", 'answer_a':"A Tricycle", 'answer_b': "B Trick Daddy", 'answer_c': "C Triceratops", 'correct_answer': "A"}, 
    {"question":"What word does Aretha Franklin spell out in her iconic 1967 hit?", 'answer_a':"A Respect", 'answer_b': "B Robocop", 'answer_c': "C Ridonkulous", 'correct_answer': "A"},
    {"question":"What Canadian province's name is Latin for 'New Scotland'?", 'answer_a': "A Nova Scotia", 'answer_b': "B Ontario", 'answer_c': "C Alberta", 'correct_answer': "A"},
    {"question":"Which of these speeds is typically fastest?", "answer_a":"A Speed of light", "answer_b":"B Speed of sound", "answer_c":"C They're the same", "correct_answer":"A"},
    {"question":"Three consecutive strikes is known as a turkey in which of these sports?", "answer_a":"A Bowling", "answer_b":"B Cricket", "answer_c":"C Volleyball", "correct_answer":"A"},
    {"question":"At the start of his career, Justin Bieber was mentored by which of these musicians?", "answer_a":"A Jay-Z", "answer_b":"B Usher", "answer_c":"C DJ Khaled", "correct_answer":"B"},
    {"question":"By definition, which of these words can refer to a college graduation ceremony?", "answer_a":"A Initiation", "answer_b":"B Matriculation", "answer_c":"C Commencement", "correct_answer":"C"},
    {"question":"Which of these baseball pitches puts the least spin on the ball?", "answer_a":"A Curveball", "answer_b":"B Knuckleball", "answer_c":"C Fastball", "correct_answer":"B"},
    {"question":"The name of Shakespeare's only son is one letter off from the title of what play?", "answer_a":"A Macbeth", "answer_b":"B Hamlet", "answer_c":"C Othello", "correct_answer":"B"},
    {"question":"Which of these terms comes from a French phrase that means 'come help me'?", "answer_a":"A SOS", "answer_b":"B Ahoy", "answer_c":"C Mayday", "correct_answer":"C"},
]

db.connect()
db.drop_tables([Question])
db.create_tables([Question])

for list_element in question_data:
    # print(list_element['question'])
    list_element = Question(question = list_element['question'], answer_a = list_element['answer_a'], answer_b = list_element['answer_b'], answer_c = list_element['answer_c'], correct_answer = list_element['correct_answer'])
    list_element.save()

def game():
    question_list = Question.select()
    for game_question in question_list:
        print(f'{game_question.question} {game_question.answer_a}, {game_question.answer_b}, or {game_question.answer_c}')
        guess= input("Enter A, B, or C! ")
        if(guess == game_question.correct_answer):
            print(f"Good job! The correct answer was {game_question.correct_answer}!")
            game_question.card_count = game_question.card_count + 1
        elif(guess != game_question.correct_answer):
            print(f"Not quite! The correct answer was {game_question.correct_answer}.")

user = input("To creat a card press C, to Quiz yourself, press G! ")
if(user == "C"):
    question = input("Enter your question! ")
    answer_a = input("Enter answer A ")
    answer_b = input("Enter answer B ")
    answer_c = input("Enter answer C ")
    correct_answer = input("Enter the letter of the correct answer! ")
    new_question = Question(question = question, answer_a = answer_a, answer_b = answer_b, answer_c = answer_c, correct_answer = correct_answer)
    new_question.save()
    
if(user == "G"):
    game()
   






# question_1 = Question()
# question_1.save()
# question_2 = Question()
# question_2.save()

# print(f"{question_1.question} {question_1.answer_a}, {question_1.answer_b}, or {question_1.answer_c}")
# guess= input("Enter A, B, or C! ")
# if(guess == question_1.correct_answer):
#     print(f"Good job! The correct answer was {question_1.correct_answer}!")
# else:
#     print(f"Not quite! The correct answer was {question_1.correct_answer}.")