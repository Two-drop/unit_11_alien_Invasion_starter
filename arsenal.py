import pygame
from bullet import Bullet
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Arsenal:
    """Class that handles the ship's ammunition"""
    def __init__(self, game: 'AlienInvasion') -> None:
        """Initializes the ship's arsenal settings

        Args:
            game (AlienInvasion): references the Alien Invasion main file
        """
        self.game = game
        self.settings = game.settings
        self.arsenal = pygame.sprite.Group()

    def update_arsenal(self) -> None:
        """Updates the arsenal's bullets"""
        self.arsenal.update()
        self._remove_bullets_offscreen()

    def _remove_bullets_offscreen(self) -> None:
        """Removes offscreen bullets to allow shooting of new ones"""
        for bullet in self.arsenal.copy():
            if bullet.rect.bottom <= 0:
                self.arsenal.remove(bullet)

    def draw(self) -> None:
        """Draws the bullets onto the screen"""
        for bullet in self.arsenal:
            bullet.draw_bullet()
    
    def fire_bullet(self) -> bool:
        """Checks to see if there are enough bullets in arsenal

        Returns:
            bool: If not enough bullets then you can't shoot anymore, else you
            can continue shooting.
        """
        if len(self.arsenal) < self.settings.bullet_amount:
            new_bullet = Bullet(self.game)
            self.arsenal.add(new_bullet)
            return True
        
        return False