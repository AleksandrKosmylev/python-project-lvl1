import random
"""yes = even, no = odd"""


def even():
    rules = 'Answer "yes" if the number is even, otherwise answer "no".'
    task = random.randint(0, 1000000)
    if task % 2 == 0:
        answer = "yes"
    else:
        answer = "no"
    return rules, task, answer
