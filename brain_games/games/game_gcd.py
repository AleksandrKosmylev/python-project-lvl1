import random
max_value = 100


def get_gcd_rules():
    return 'Find the greatest common divisor of given numbers.'


def get_gcd_round():
    num1 = random.randint(1, max_value)
    num2 = random.randint(1, max_value)
    task = str(num1) + ' ' + str(num2)
    for j in range(1, num1 + 1):
        if num1 % j == 0 and num2 % j == 0:
            answer = str(j)
    return task, answer
