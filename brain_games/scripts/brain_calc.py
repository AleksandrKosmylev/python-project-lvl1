#!/usr/bin/env python

from games.game_calc import rules, task, user_answer, answer
from games.logic import game

def main():
    game(rules, task,  user_answer, answer)


if __name__ == '__main__':
    main()
