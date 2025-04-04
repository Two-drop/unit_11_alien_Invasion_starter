""" Alien Invasion
    author: Noah Kattner
    date: 04/03/2025
    Game where you control a space ship and shoot lasers
"""

import sys
import pygame
from settings import Settings
from ship import Ship
from arsenal import Arsenal


class AlienInvasion():
    """Class that will handle the launching and main functionalities of the game"""
    def __init__(self) -> None:
        """Main function to initialize the game with its settings"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_w, self.settings.screen_h)
            )
        pygame.display.set_caption(self.settings.name)
        
        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(self.bg,
            (self.settings.screen_w, self.settings.screen_h)
            )

        self.running = True
        self.clock = pygame.time.Clock()

        pygame.mixer.init()
        self.laser_sound = pygame.mixer.Sound(self.settings.laser_sound)
        self.laser_sound.set_volume(0.6)

        self.ship = Ship(self, Arsenal(self))
        

    def run_game(self) -> None:
        """Allows the game to continue running with a loop"""
        while self.running:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(self.settings.FPS)

    def _update_screen(self) -> None:
        """Displays the background and ship onto the screen."""
        self.screen.blit(self.bg, (0,0))
        self.ship.draw()
        pygame.display.flip()

    def _check_events(self) -> None:
        """Allows to quit the game and checks the status of the key pressed"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    def _check_keydown_events(self, event) -> None:
        """Moves the ship, plays a sound and exits game based on what key 
        is being pressed on a keyboard"""
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_SPACE:
            if self.ship.fire():
                self.laser_sound.play()
                self.laser_sound.fadeout(250)
        elif event.key == pygame.K_q:
            self.running = False
            pygame.quit()
            sys.exit()

    def _check_keyup_events(self, event) -> None:
        """Stops the ship from moving if a key is let go off."""
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
