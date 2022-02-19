#!/usr/bin/env python
from brain_games.games.logic import game
from brain_games.games.game_even import get_even_rules, get_even_round


def main():
    game(get_even_rules, get_even_round)


if __name__ == '__main__':
    main()
