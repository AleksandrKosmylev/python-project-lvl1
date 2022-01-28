#!/usr/bin/env python
from brain_games import game_calc
from brain_games import logic

n = game_calc.name
r = game_calc.rules
t = game_calc.task
u = game_calc.user_answer
a = game_calc.answer
def main():
    print('Welcome to the Brain Games!')
    logic.game(n, r, t, u, a)


if __name__ == '__main__':
    main()
