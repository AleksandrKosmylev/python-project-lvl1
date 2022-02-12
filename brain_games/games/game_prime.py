import random

rules = 'Answer "yes" if given number is prime. Otherwise answer "no"'
task = [random.randint(1, 100) for i in range(3)]
answer = []
for i in task:
    if i == 1 or i == 2:
        answer.append("yes")
    else:
        for j in range(2, i + 1):
            if i % j == 0 and i != j:
                answer.append("no")
                break
            elif i == j:
                answer.append("yes")
