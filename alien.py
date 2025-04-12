# alien.py
# author: Noah Kattner
# date: 04/03/2025

import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Lab13_nkattner_1 import AlienInvasion

class Alien(Sprite):
    """Class that contains information regarding how a alien will work"""
    def __init__(self, game: 'AlienInvasion', x: float, y: float) -> None:
        """Initializes the ship's alien settings and collision

        Args:
            game (AlienInvasion): references the Alien Invasion main file
        """
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.boundaries = game.screen
        self.settings = game.settings

        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(self.image,
            (self.settings.alien_w, self.settings.alien_h)
            )
        self.image = pygame.transform.rotate(self.image, 90)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # self.x = float(self.rect.x)
    
    def update(self) -> None:
        """Handles the speed and direction of the alien"""
        # self.x += self.settings.fleet_speed
        # self.rect.x = self.x
        pass

    def draw_alien(self) -> None:
        """Allows the aliens to be drawn on screen"""
        self.screen.blit(self.image, self.rect)