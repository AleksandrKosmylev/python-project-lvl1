import random
"""yes = even, no = odd"""


rules = 'Answer "yes" if the number is even, otherwise answer "no".'
task = [random.randint(0, 1000000) for i in range(3)]
list = []
for i in task:
    if i % 2 == 0:
        list.append("yes")
    else:
        list.append("no")
answer = list[:]
