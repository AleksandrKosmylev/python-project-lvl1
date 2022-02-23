import random
from brain_games.logic import run_game
max_value_for_num = 10


def get_calc_description():
    return 'What is the result of the expression?'


def get_calc_round():
    num1 = random.randint(0, max_value_for_num)
    num2 = random.randint(0, max_value_for_num)
    rand_signs = random.choice(['*', '+', '-'])
    task = str(num1) + ' ' + rand_signs + ' ' + str(num2)
    if rand_signs == '*':
        answer = str(num1 * num2)
    elif rand_signs == '+':
        answer = str(num1 + num2)
    else:
        answer = str(num1 - num2)
    return task, answer


def run_game_calc():
    run_game(get_calc_description, get_calc_round)
