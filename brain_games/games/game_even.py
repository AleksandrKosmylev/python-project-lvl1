import random
"""yes = even, no = odd"""


def even_rules():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def even_game():
    max_value = 1000000
    task = random.randint(0, max_value)
    if task % 2 == 0:
        answer = "yes"
    else:
        answer = "no"
    return task, answer
