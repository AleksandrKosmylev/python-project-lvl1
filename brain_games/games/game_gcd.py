import random


def gcd():
    rules = 'Find the greatest common divisor of given numbers.'
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    task = str(num1) + ' ' + str(num2)
    for j in range(1, num1 + 1):
        if num1 % j == 0 and num2 % j == 0:
            answer = str(j)
    return rules, task, answer
