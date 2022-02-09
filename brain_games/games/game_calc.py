import random


rules = 'What is the result of the expression?'
num1 = [random.randint(0, 10) for i in range(3)]
num2 = [random.randint(0, 10) for i in range(3)]
rand_signs = [random.choice(['*', '+']) for i in range(3)]
list_for_task = []
list_for_answer = []
for i in range(3):
    variable = str(num1[i]) + ' ' + rand_signs[i] + ' ' + str(num2[i])
    list_for_task.append(variable)
    if rand_signs[i] == '*':
        list_for_answer.append(str(num1[i] * num2[i]))
    elif rand_signs[i] == '+':
        answer = num1[i] + num2[i]
        list_for_answer.append(str(num1[i] + num2[i]))
task = list_for_task[:]
answer = list_for_answer[:]
