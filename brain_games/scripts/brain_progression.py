#!/usr/bin/env python
from brain_games.games.logic import game
from brain_games.games.game_progression import get_progression_rules
from brain_games.games.game_progression import get_progression_round


def main():
    game(get_progression_rules, get_progression_round)


if __name__ == '__main__':
    main()
