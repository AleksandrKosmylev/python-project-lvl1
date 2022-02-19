#!/usr/bin/env python
from brain_games.games.logic import game
from brain_games.games.game_even import even_rules, even_game


def main():
    game(even_rules, even_game)


if __name__ == '__main__':
    main()
