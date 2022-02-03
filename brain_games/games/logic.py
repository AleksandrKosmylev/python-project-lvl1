def game(rules, task, answer):
    print('Welcome to the Brain Games!')
    print('May I have your name? ')
    name = input()
    print(rules)
    counter = 0
    while counter < 3:
        print(f"Question: {task[counter]}")
        user_answer = input("Your answer: ")
        if user_answer == answer[counter]:
            counter = counter + 1
        else:
            break
    if counter == 3:
        print(f"Congratulations, {name}")
    else:
        print(f"{user_answer} is wrong(. Correct answer was {answer[counter]}.")
