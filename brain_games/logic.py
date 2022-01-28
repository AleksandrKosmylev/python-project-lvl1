def game(n, r, t, u, a):
    print(n, r, t)
    counter = 0
    while counter < 3:
        if u == a:
            counter = counter + 1
            print(t)
        else:
            break
    if counter == 3:
        print(f"Congratulations, {n}")
    else:
        print(f"{u} is wrong(. Correct answer was {a}.")
