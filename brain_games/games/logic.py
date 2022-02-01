def game(rules):
    print('Welcome to the Brain Games!')
    print('May I have your name? ')
    name = input()
    print(rules)
    print(task)
    counter = 0
    while counter < 3:
        if user_answer == answer:
            counter = counter + 1
            print(task)
        else:
            break
    if counter == 3:
        print(f"Congratulations, {name}")
    else:
        print(f"{user_answer} is wrong(. Correct answer was {answer}.")
