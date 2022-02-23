import random
from brain_games.logic import run_game
max_num_task = 100


def get_prime_task():
    return 'Answer "yes" if given number is prime. Otherwise answer "no"'


def is_prime(value):
    if value == 1 or value == 2:
        return True
    else:
        for j in range(2, value + 1):
            if value % j == 0 and value != j:
                return False
        return True


def get_prime_round():
    task = random.randint(1, max_num_task)
    if is_prime(task):
        answer = "yes"
    else:
        answer = "no"
    return task, answer


def run_game_prime():
    run_game(get_prime_task, get_prime_round)
