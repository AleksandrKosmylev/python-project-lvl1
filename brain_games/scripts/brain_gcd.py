#!/usr/bin/env python
from brain_games.games.logic import game
from brain_games.games.game_gcd import get_gcd_rules, get_gcd_round


def main():
    game(get_gcd_rules, get_gcd_round)


if __name__ == '__main__':
    main()
