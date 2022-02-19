#!/usr/bin/env python
from brain_games.games.logic import game
from brain_games.games.game_calc import calc_rules, calc_game


def main():
    game(calc_rules, calc_game)


if __name__ == '__main__':
    main()
