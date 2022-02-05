import prompt


def game(rules, task, answer):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(rules)
    counter = 0
    while counter < 3:
        print(f"Question: {task[counter]}")
        user_answer = input("Your answer: ")
        if user_answer == answer[counter]:
            counter = counter + 1
            print("Correct!")
        else:
            break
    if counter == 3:
        print(f"Congratulations, {name}")
    else:
        print(f"{user_answer} is wrong(. Correct answer was {answer[counter]}.")
        print(f"Let's try again,{name}")
