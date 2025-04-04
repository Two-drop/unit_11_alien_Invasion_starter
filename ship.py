# ship.py
# author: Noah Kattner
# date: 04/03/2025

import pygame
from typing import TYPE_CHECKING
if TYPE_CHECKING:
     from Lab12_nkattner_1 import AlienInvasion
     from arsenal import Arsenal

class Ship:
     """Class to store information for ship actions and display"""
     def __init__(self, game: 'AlienInvasion', arsenal: 'Arsenal') -> None:
          """Initializes the ship and screen boundaries

          Args:
              game (AlienInvasion): It can access the Alien Invasion game data
              arsenal (Arsenal): It accesses the arsenal file data.
          """
          self.game = game
          self.settings = game.settings
          self.screen = game.screen
          self.boundaries = self.screen.get_rect()
          
          self.image = pygame.image.load(self.settings.ship_file)
          self.image = pygame.transform.scale(self.image,
               (self.settings.ship_w, self.settings.ship_h)
               )
          
          self.rect = self.image.get_rect()
          self.rect.midbottom = self.boundaries.midbottom
          self.moving_right = False
          self.moving_left = False
          self.x = float(self.rect.x)
          self.arsenal = arsenal

     def update(self) -> None:
          """Updates the movement and arsenal of the ship"""
          self._update_ship_movement()
          self.arsenal.update_arsenal()
     

     def _update_ship_movement(self) -> None:
         """Manages the ship's speed and direction within the screen's 
         boundaries"""
         temp_speed = self.settings.ship_speed
         if self.moving_right and self.rect.right < self.boundaries.right:
              self.x += temp_speed
         if self.moving_left and self.rect.left > self.boundaries.left:
              self.x -= temp_speed
          
         self.rect.x = self.x

     def draw(self) -> None:
          """Displays the ship's bullets on the screen"""
          self.arsenal.draw()
          self.screen.blit(self.image, self.rect)

     def fire(self) -> bool:
          """Ability to fire bullets from the arsenal

          Returns:
              bool: Checks to see if you can continue shooting
          """
          return self.arsenal.fire_bullet()