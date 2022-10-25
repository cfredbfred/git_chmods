#!/usr/bin/env python3

import pygame
import config
from game import Game, game_init
from game_state import GameState

def main():
    game, clock = game_init()
    while game.game_state == GameState.RUNNING:

        clock.tick(50)
        game.update()
        pygame.display.flip()


if __name__ == '__main__':
    main()

