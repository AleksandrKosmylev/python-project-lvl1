import random
max_value_for_num = 10


def get_calc_rule():
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
