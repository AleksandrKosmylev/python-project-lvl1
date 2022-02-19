#!/usr/bin/env python
from brain_games.games.logic import game
from brain_games.games.game_prime import get_prime_rules, get_prime_round


def main():
    game(get_prime_rules, get_prime_round)


if __name__ == '__main__':
    main()
