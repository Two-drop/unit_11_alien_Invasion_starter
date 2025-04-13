# alien_fleet.py
# author: Noah Kattner
# date: 04/12/2025

import pygame
from typing import TYPE_CHECKING
from alien import Alien
if TYPE_CHECKING:
    from Lab13_nkattner_1 import AlienInvasion

class AlienFleet:
     
    def __init__(self, game: 'AlienInvasion'):
        self.game = game
        self.settings = game.settings
        self.fleet = pygame.sprite.Group()
        self.fleet_direction = self.settings.fleet_direction
        self.fleet_drop_speed = self.settings.fleet_drop_speed

        self.create_fleet()
    
    def create_fleet(self):
        alien_h = self.settings.alien_h
        alien_w = self.settings.alien_w
        screen_h = self.settings.screen_h
        screen_w = self.settings.screen_w

        fleet_h = self.calculate_fleet_size(alien_h, screen_h)

        
        fleet_vertical_space = fleet_h + alien_h
        y_offset = int((fleet_vertical_space)//2)

        for col in range(fleet_h):
            current_y = (alien_h * col) + y_offset
            if col % 2 == 0:
                continue
            self._create_alien(10, current_y)
    
    def calculate_fleet_size(self, alien_h, screen_h):
        fleet_h = (screen_h//alien_h)

        if fleet_h % 2 == 0:
            fleet_h -= 1
        else:
            fleet_h -= 2
        
        return fleet_h
    
    def _create_alien(self, current_x: int, current_y: int):
        new_alien = Alien(self, current_x, current_y)

        self.fleet.add(new_alien)

    def draw(self):
        alien: 'Alien'
        for alien in self.fleet:
            alien.draw_alien()