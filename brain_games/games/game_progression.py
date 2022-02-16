import random


def progression():
    rules = 'What number is missing in the progression?'
    step = random.randint(1, 10)
    start = random.randint(0, 100)
    position = random.randint(0, 9)
    number_in_prog = start
    progression = [number_in_prog]
    for o in range(9):
        number_in_prog = number_in_prog + step
        progression.append(number_in_prog)
    str_of_numbers = ''
    answer = str(progression[position])
    progression[position] = '..'
    for c in progression:
        str_of_numbers = str_of_numbers + " " + str(c)
    task = str_of_numbers[1:]
    return rules, task, answer
