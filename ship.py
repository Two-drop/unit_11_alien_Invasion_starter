# ship.py
# author: Noah Kattner
# date: 04/03/2025

import pygame
from typing import TYPE_CHECKING
if TYPE_CHECKING:
     from Lab13_nkattner_1 import AlienInvasion
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
          self.image = pygame.transform.rotate(self.image, 90)
          
          self.rect = self.image.get_rect()
          self._center_ship()
          self.moving_down = False
          self.moving_up = False
          self.arsenal = arsenal

     def _center_ship(self):
         self.rect.right = self.boundaries.right
         self.rect.centery = self.boundaries.centery
         self.y = float(self.rect.y)

     def update(self) -> None:
          """Updates the movement and arsenal of the ship"""
          self._update_ship_movement()
          self.arsenal.update_arsenal()
     

     def _update_ship_movement(self) -> None:
         """Manages the ship's speed and direction within the screen's 
         boundaries"""
         temp_speed = self.settings.ship_speed
         if self.moving_down and self.rect.bottom < self.boundaries.bottom:
              self.y += temp_speed
         if self.moving_up and self.rect.top > self.boundaries.top:
              self.y -= temp_speed
          
         self.rect.y = self.y

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
     
     def check_collisions(self, other_group) -> bool:
          """Checks if aliens collide with player ship and resets ship

          Arguments:
              other_group -- other objects in the sprite group

          Returns:
              bool: if there is a collision returns true, else false
          """
          if pygame.sprite.spritecollideany(self, other_group):
               self._center_ship()
               return True
          return False