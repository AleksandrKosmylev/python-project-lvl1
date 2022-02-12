import random

rules = 'What number is missing in the progression?'
step = [random.randint(1, 9) for i in range(3)]
start = [random.randint(0, 100) for j in range(3)]
position = [random.randint(0, 10) for k in range(3)]
task_list = []
task = []
answer = []
for d in range(3):
    number_in_prog = start[d]
    progression = [number_in_prog]
    for o in range(9):
        number_in_prog = number_in_prog + step[d]
        progression.append(number_in_prog)
    task_list.append(progression)
for z in range(3):
    str_of_numbers = ''
    number = step[z]
    answer.append(str(task_list[z][number]))
    task_list[z][number] = '..'
    for c in task_list[z]:
        str_of_numbers = str_of_numbers + " " + str(c)
    task.append(str_of_numbers)
