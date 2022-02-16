import prompt


def game(get_values):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    rules, task, answer = get_values()
    print(rules)
    counter = 0
    while counter < 3:
        rules, task, answer = get_values()
        print(f"Question: {task}")
        user_answer = input("Your answer: ")
        if user_answer == answer:
            counter = counter + 1
            print("Correct!")
        else:
            break
    if counter == 3:
        print(f"Congratulations, {name}!")
    else:
        print(f"'{user_answer}' is wrong ;(.", end=" ")
        print(f"Correct answer was '{answer}'.")
        print(f"Let's try again, {name}!")
