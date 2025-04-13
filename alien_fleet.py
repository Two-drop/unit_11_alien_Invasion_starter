# alien_fleet.py
# author: Noah Kattner
# date: 04/12/2025

import pygame
from typing import TYPE_CHECKING
from alien import Alien
if TYPE_CHECKING:
    from Lab13_nkattner_1 import AlienInvasion

class AlienFleet:
    """ Class to handle all display settings and movement for the alien fleet
    """
    def __init__(self, game: 'AlienInvasion') -> None:
        """Initializes the alien fleet's settings and creation

        Arguments:
            game -- References the AlienInvasion game's main file
        """
        self.game = game
        self.settings = game.settings
        self.fleet = pygame.sprite.Group()
        self.fleet_direction = self.settings.fleet_direction
        self.fleet_drop_speed = self.settings.fleet_drop_speed

        self.create_fleet()
    
    def create_fleet(self) -> None:
        """ Creates the alien fleet with its appropriate dimensions and offsets
        """
        alien_h = self.settings.alien_h
        alien_w = self.settings.alien_w
        screen_h = self.settings.screen_h
        screen_w = self.settings.screen_w

        fleet_h, fleet_w = self.calculate_fleet_size(alien_h, screen_h, alien_w, screen_w)
        
        y_offset, x_offset = self.calculate_offsets(alien_h, alien_w, fleet_h, fleet_w)

        self._create_rectangle_fleet(alien_h, alien_w, fleet_h, fleet_w, y_offset, x_offset)

    def _create_rectangle_fleet(self, alien_h, alien_w, fleet_h, fleet_w, y_offset, x_offset) -> None:
        """Creates each alien ship within a fleet spaced out evenly

        Arguments:
            alien_h -- height of the alien ship
            alien_w -- width of the alien ship
            fleet_h -- the height of the entire fleet
            fleet_w -- the width of the entire fleet
            y_offset -- the vertical space between each alien ship
            x_offset -- the horizontal space between each alien ship
        """
        for col in range(fleet_w):
            for row in range(fleet_h):
                current_y = (alien_h * row) + y_offset
                current_x = (alien_w * col) + x_offset
                if row % 2 == 0 or col % 2 == 0:
                    continue
                self._create_alien(current_x, current_y)

    def calculate_offsets(self, alien_h, alien_w, fleet_h, fleet_w) -> int:
        """ Calculates the space each alien ship should have from each other

        Arguments:
            alien_h -- height of the alien ship
            alien_w -- width of the alien ship
            fleet_h -- the height of the entire fleet
            fleet_w -- the width of the entire fleet

        Returns:
            int: The y and x offsets between each alien ship within the fleet
        """
        fleet_vertical_space = fleet_h + alien_h
        fleet_horizontal_space = fleet_w + alien_w
        y_offset = int((fleet_vertical_space)//2)
        x_offset = int((fleet_horizontal_space)//2)
        return y_offset, x_offset
    
    def calculate_fleet_size(self, alien_h, screen_h, alien_w, screen_w) -> int:
        """ Calculates the fleet's size

        Arguments:
            alien_h -- height of the alien ship
            screen_h -- display screen's width
            alien_w -- width of the alien ship
            screen_w -- display screen's height

        Returns:
            int: Fleet's height and width
        """
        fleet_h = (screen_h//alien_h)
        fleet_w = ((screen_w / 2)//alien_w)

        if fleet_h % 2 == 0:
            fleet_h -= 1
        else:
            fleet_h -= 2

        if fleet_w % 2 == 0:
            fleet_w -= 1
        else:
            fleet_w -= 2
        
        return int(fleet_h), int(fleet_w)
    
    def _create_alien(self, current_x: int, current_y: int) -> None:
        """ Creates each alien in the fleet

        Arguments:
            current_x -- current alien ship's location in x position
            current_y -- current alien ship's location in y position
        """
        new_alien = Alien(self, current_x, current_y)

        self.fleet.add(new_alien)

    def _check_fleet_edges(self) -> None:
        """ Checks to see if the fleet has touched the horizontal border of
        the screen and moves the fleet down and opposite y direction
        """
        alien: Alien
        for alien in self.fleet:
            if alien.check_edges():
                self._drop_alien_fleet()
                self.fleet_direction *= -1
                break

    def _drop_alien_fleet(self) -> None:
        """ Moves the fleet towards the right
        """
        for alien in self.fleet:
            alien.x += self.fleet_drop_speed

    def update_fleet(self) -> None:
        """ Updates the fleet's movement
        """
        self._check_fleet_edges()
        self.fleet.update()
    
    def draw(self) -> None:
        """ Draws each alien ship
        """
        alien: Alien
        for alien in self.fleet:
            alien.draw_alien()