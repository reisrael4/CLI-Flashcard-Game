from peewee import *
from ques_db import Question

db = PostgresqlDatabase('questions', user='postgres', password='', host='localhost', port=5432)

def game():
    question_list = Question.select()
    count = 0
    for game_question in question_list:
        print(f'{game_question.question} {game_question.answer_a}, {game_question.answer_b}, or {game_question.answer_c}')
        guess= input("Enter A, B, or C! ")

#It's this section

        if(guess == game_question.correct_answer):
            count = count + 1
            game_question.card_count = int(game_question.card_count + 1)
            game_question.save()
            print(f"Good job! The correct answer was {game_question.correct_answer}! You have gotten that card correct {game_question.card_count} times")

###
            
        elif(guess != game_question.correct_answer):
            print(f"Not quite! The correct answer was {game_question.correct_answer}.")
    if game_question != len(question_list) - 1:
        play_again = input(f"Good game! You got {count} questions correct! Would you like to play again? y/n ")
        if play_again == 'y':
            game()

user = input("To creat a card press C, to Quiz yourself, press G! ")
if(user == "C"):
    question = input("Enter your question! ")
    answer_a = input("Enter answer starting with A ")
    answer_b = input("Enter answer starting with B ")
    answer_c = input("Enter answer starting with C ")
    correct_answer = input("Enter the letter of the correct answer! ")
    new_question = Question(question = question, answer_a = answer_a, answer_b = answer_b, answer_c = answer_c, correct_answer = correct_answer, card_count = 0)
    new_question.save()
    game_input = input("Would you like to play the game? y/n ")
    if(game_input == "y"):
        game()
    
if(user == "G"):
    game()