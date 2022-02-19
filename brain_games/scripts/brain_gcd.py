#!/usr/bin/env python
from brain_games.games.logic import game
from brain_games.games.game_gcd import gcd_rules, gcd_game


def main():
    game(gcd_rules, gcd_game)


if __name__ == '__main__':
    main()
