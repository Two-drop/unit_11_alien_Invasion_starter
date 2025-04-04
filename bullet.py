import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

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
        
        self.rect = self.image.get_rect()
        self.rect.midtop = game.ship.rect.midtop
        self.y = float(self.rect.y)
    
    def update(self) -> None:
        """Handles the speed and direction of the bullet"""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self) -> None:
        """Allows the bullets to be drawn on screen"""
        self.screen.blit(self.image, self.rect)