import random


def gcd():
    max_value = 100
    rules = 'Find the greatest common divisor of given numbers.'
    num1 = random.randint(1, max_value)
    num2 = random.randint(1, max_value)
    task = str(num1) + ' ' + str(num2)
    for j in range(1, num1 + 1):
        if num1 % j == 0 and num2 % j == 0:
            answer = str(j)
    return rules, task, answer
