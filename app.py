from Question import Question
from Choice import Choice
import random
q_and_a = open("QandA.txt", "r")
quiz = q_and_a.readlines()
quiz_length = len(quiz) - 1
questions = []

def make_choices(question):
    a = random.randint(0,2)

    if a == 0:
        correct_choice = "a"
        choice_a = question.correct_answer
        choice_b = question.other_choice1
        choice_c = question.other_choice2
    elif a == 1:
        correct_choice = "b"
        choice_a = question.other_choice1
        choice_b = question.correct_answer
        choice_c = question.other_choice2
    else:
        correct_choice = "c"
        choice_a = question.other_choice2
        choice_b = question.other_choice1
        choice_c = question.correct_answer
    selections = Choice(correct_choice, choice_a, choice_b, choice_c)
    return selections


for entry in range(0, quiz_length, 4):
    query = Question(quiz[entry], quiz[entry + 1], quiz[entry + 2], quiz[entry + 3])
    questions.append(query)

score = 0
for question in questions:
    ask = question.prompt
    choices = make_choices(question)
    the_question_and_choices = str(ask) + "\n" + "a. " + str(choices.choice_a) + "b. " + str(choices.choice_b) + "c. " + str(choices.choice_c) + "\n >"
    user_input = input(the_question_and_choices)
    print(user_input)
    if user_input == str(choices.correct_choice):
        score += 1
    else:
        score = score

print("You got " + str(score) + " out of " + str(quiz_length/4))




