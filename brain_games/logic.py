import prompt
number_of_rounds = 3


def run_game(get_rules, get_game_round):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    rules = get_rules()
    print(rules)
    counter = 0
    while counter < number_of_rounds:
        task, answer = get_game_round()
        print(f"Question: {task}")
        user_answer = input("Your answer: ")
        if user_answer == answer:
            counter = counter + 1
            print("Correct!")
        else:
            break
    if counter == number_of_rounds:
        print(f"Congratulations, {name}!")
    else:
        print(f"'{user_answer}' is wrong ;(.", end=" ")
        print(f"Correct answer was '{answer}'.")
        print(f"Let's try again, {name}!")
