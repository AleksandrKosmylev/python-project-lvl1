import random


def get_calc_rules():
    return 'What is the result of the expression?'


def get_calc_round():
    max_value_for_num = 10
    num1 = random.randint(0, max_value_for_num)
    num2 = random.randint(0, max_value_for_num)
    rand_signs = random.choice(['*', '+'])
    task = str(num1) + ' ' + rand_signs + ' ' + str(num2)
    if rand_signs == '*':
        answer = str(num1 * num2)
    elif rand_signs == '+':
        answer = str(num1 + num2)
    return task, answer
