import random
from brain_games.logic import game
max_value = 100


def get_gcd_rules():
    return 'Find the greatest common divisor of given numbers.'


def get_gcd(num1, num2):
    for j in range(1, num1 + 1):
        if num1 % j == 0 and num2 % j == 0:
            answer = str(j)
    return answer


def get_gcd_round():
    num1 = random.randint(1, max_value)
    num2 = random.randint(1, max_value)
    task = str(num1) + ' ' + str(num2)
    answer = get_gcd(num1, num2)
    return task, answer


def run_game_gcd():
    game(get_gcd_rules, get_gcd_round)
