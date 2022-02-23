import random
from brain_games.logic import run_game
max_progression_step = 10
max_first_num = 100
length_of_progression = 9


def get_progression_rule():
    return 'What number is missing in the progression?'


def get_progression_round():
    step = random.randint(1, max_progression_step)
    start = random.randint(0, max_first_num)
    position = random.randint(0, length_of_progression)
    number_in_prog = start
    progression = [number_in_prog]
    for _ in range(length_of_progression):
        number_in_prog = number_in_prog + step
        progression.append(number_in_prog)
    str_of_numbers = ''
    answer = str(progression[position])
    progression[position] = '..'
    for c in progression:
        str_of_numbers = str_of_numbers + " " + str(c)
    task = str_of_numbers[1:]
    return task, answer


def run_game_progression():
    run_game(get_progression_rule, get_progression_round)
