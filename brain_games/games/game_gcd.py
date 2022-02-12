import random


rules = 'Find the greatest common divisor of given numbers.'
num1 = [random.randint(1, 100) for i in range(3)]
num2 = [random.randint(1, 100) for c in range(3)]
task = []
answer = []
deviders = []
for k in range(3):
    # add task to the task list
    task.append(str(num1[k]) + ' ' + str(num2[k]))
for x in range(3):
    for j in range(1, num1[x] + 1):
        if num1[x] % j == 0 and num2[x] % j == 0:
            deviders = str(j)
    answer.append(deviders)
