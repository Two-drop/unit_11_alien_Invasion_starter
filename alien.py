# alien.py
# author: Noah Kattner
# date: 04/12/2025

import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from alien_fleet import AlienFleet

class Alien(Sprite):
    """Class that will control alien ship's movement on screen"""
    def __init__(self, fleet: 'AlienFleet', x: float, y: float) -> None:
        """Initializes the alien's settings and collision

        Args:
            game (AlienInvasion): references the Alien Invasion main file
        """
        super().__init__()
        self.fleet = fleet
        self.screen = fleet.game.screen
        self.boundaries = fleet.game.screen.get_rect()
        self.settings = fleet.game.settings

        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(self.image,
            (self.settings.alien_w, self.settings.alien_h)
            )
        self.image = pygame.transform.rotate(self.image, 90)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
    
    def update(self) -> None:
        """Handles the speed and direction of the alien within the screen's
        boundaries"""
        temp_speed = self.settings.fleet_speed
        self.y += temp_speed * self.fleet.fleet_direction
        self.rect.y = self.y
        self.rect.x = self.x


    def check_edges(self) -> bool:
        ''' Checks to see if the alien's ship hits an edge of the screen
        
        Returns:
            bool: Return true if the alien hits one of the edges
        '''
        return (self.rect.bottom >= self.boundaries.bottom or 
                self.rect.top <= self.boundaries.top)

    def draw_alien(self) -> None:
        """Allows the aliens to be drawn on screen"""
        self.screen.blit(self.image, self.rect)