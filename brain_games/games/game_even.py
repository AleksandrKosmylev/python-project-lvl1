import random
"""yes = even, no = odd"""


def even():
    max_value = 1000000
    rules = 'Answer "yes" if the number is even, otherwise answer "no".'
    task = random.randint(0, max_value)
    if task % 2 == 0:
        answer = "yes"
    else:
        answer = "no"
    return rules, task, answer
