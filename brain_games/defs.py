import prompt
import random

def game():
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    counter = 0
    while counter < 3:
        print('Answer "yes" if the number is even, otherwise answer "no".')
        b = random.randint(0, 1000000)
        print(f'Question :{b}')
        if b%2 == 0:
        #yes = even, no = odd
            num = "yes"
        else:
            num = "no"
        a = input("Your answer:")
        if a == num:
            print("Correct!")
            counter = counter +1
        else:
            print(f"{a} is wrong answer ;(. Correct answer was {num}.")
            counter = 0
    print(f"Congratulations, {name}")