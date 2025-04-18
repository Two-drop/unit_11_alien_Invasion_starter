"""bullet.py
author: Noah Kattner
date: 04/03/2025"""

import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Lab14_nkattner_1 import AlienInvasion

class Bullet(Sprite):
    """Class that contains information regarding how a bullet will work"""
    def __init__(self, game: 'AlienInvasion') -> None:
        """Initializes the ship's bullet settings and collision

        Args:
            game (AlienInvasion): references the Alien Invasion main file
        """
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.settings = game.settings

        self.image = pygame.image.load(self.settings.bullet_file)
        self.image = pygame.transform.scale(self.image,
            (self.settings.bullet_w, self.settings.bullet_h)
            )
        self.image = pygame.transform.rotate(self.image, 90)

        self.rect = self.image.get_rect()
        self.rect.midleft = game.ship.rect.midleft
        self.x = float(self.rect.x)
    
    def update(self) -> None:
        """Handles the speed and direction of the bullet"""
        self.x -= self.settings.bullet_speed
        self.rect.x = self.x

    def draw_bullet(self) -> None:
        """Allows the bullets to be drawn on screen"""
        self.screen.blit(self.image, self.rect)