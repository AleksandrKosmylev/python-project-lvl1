import prompt
import random

"""yes = even, no = odd"""


def game():
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print('Answer "yes" if the number is even, otherwise answer "no".')
    counter = 0
    while counter < 3:
        b = random.randint(0, 1000000)
        print(f'Question :{b}')
        if b % 2 == 0:
            num = "yes"
        else:
            num = "no"
        a = input("Your answer:")
        if a == num:
            print("Correct!")
            counter = counter + 1
        else:
            print(f"{a} is wrong answer ;(. Correct answer was {num}.")
            break
    if counter == 3:
        print(f"Congratulations, {name}")
    else:
        print(f"Let's try again, {name}!")
