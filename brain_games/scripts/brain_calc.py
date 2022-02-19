#!/usr/bin/env python
from brain_games.games.logic import game
from brain_games.games.game_calc import get_calc_rules, get_calc_round


def main():
    game(get_calc_rules, get_calc_round)


if __name__ == '__main__':
    main()
