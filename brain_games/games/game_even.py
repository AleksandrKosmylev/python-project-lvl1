import random
"""yes = even, no = odd"""
max_value = 1000000


def get_even_task():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def get_even_round():
    task = random.randint(0, max_value)
    if task % 2 == 0:
        answer = "yes"
    else:
        answer = "no"
    return task, answer
