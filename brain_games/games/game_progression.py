import random


def get_progression_rules():
    return 'What number is missing in the progression?'


def get_progression_round():
    max_progression_step = 10
    max_first_num = 100
    last_position = 9
    step = random.randint(1, max_progression_step)
    start = random.randint(0, max_first_num)
    position = random.randint(0, last_position)
    number_in_prog = start
    progression = [number_in_prog]
    for o in range(last_position):
        number_in_prog = number_in_prog + step
        progression.append(number_in_prog)
    str_of_numbers = ''
    answer = str(progression[position])
    progression[position] = '..'
    for c in progression:
        str_of_numbers = str_of_numbers + " " + str(c)
    task = str_of_numbers[1:]
    return task, answer
