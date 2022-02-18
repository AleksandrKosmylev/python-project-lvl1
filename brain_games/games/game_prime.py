import random


def is_prime(value):
    if value == 1 or value == 2:
        return True
    else:
        for j in range(2, value + 1):
            if value % j == 0 and value != j:
                return False
                break
            elif value == j:
                return True


def prime():
    max_num_task = 100
    rules = 'Answer "yes" if given number is prime. Otherwise answer "no"'
    task = random.randint(1, max_num_task)
    if is_prime(task):
        answer = "yes"
    else:
        answer = "no"
    return rules, task, answer
