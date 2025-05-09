""" Alien Invasion
    author: Noah Kattner
    date: 04/03/2025
    Game where you control a space ship and shoot lasers
"""

import sys
import pygame
from settings import Settings
from game_stats import GameStats
from ship import Ship
from arsenal import Arsenal
from alien_fleet import AlienFleet
from time import sleep
from button import Button
from hud import HUD

class AlienInvasion():
    """Class that will handle the launching and main functionalities of the game"""
    def __init__(self) -> None:
        """Main function to initialize the game with its settings"""
        pygame.init()
        self.settings = Settings()
        self.settings.initialize_dynamic_settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_w, self.settings.screen_h)
            )
        pygame.display.set_caption(self.settings.name)
        
        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(self.bg,
            (self.settings.screen_w, self.settings.screen_h)
            )

        self.game_stats = GameStats(self)
        self.HUD = HUD(self)
        self.running = True
        self.clock = pygame.time.Clock()

        pygame.mixer.init()
        self.laser_sound = pygame.mixer.Sound(self.settings.laser_sound)
        self.laser_sound.set_volume(0.6)
        self.impact_sound = pygame.mixer.Sound(self.settings.impact_sound)
        self.impact_sound.set_volume(0.6)

        self.ship = Ship(self, Arsenal(self))
        self.alien_fleet = AlienFleet(self)
        self.alien_fleet.create_fleet()
        self.play_button = Button(self, 'Play')
        self.deactivate_play_button = False
        self.game_active = False
        

    def run_game(self) -> None:
        """Allows the game to continue running with a loop"""
        while self.running:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self.alien_fleet.update_fleet()
                self._check_collisions()
            self._update_screen()
            self.clock.tick(self.settings.FPS)

    def _check_collisions(self):
        """ Checks for every collision in the game
        """
        if self.ship.check_collisions(self.alien_fleet.fleet):
            self._check_game_status()
        if self.alien_fleet.check_fleet_right():
            self._check_game_status()

        collisions = self.alien_fleet.check_collisions(self.ship.arsenal.arsenal)
        if collisions:
            self.impact_sound.play()
            self.impact_sound.fadeout(500)
            self.game_stats.update(collisions)
            self.HUD.update_scores()

        if self.alien_fleet.check_destroyed_status():
            self._reset_level()
            self.settings.increase_difficulty()
            self.game_stats.update_level()
            self.HUD.update_level()
        
    def _check_game_status(self) -> None:
        """Checks to see if the player is still alive to see if damage is taken
        """
        if self.game_stats.ships_left > 0:
            self.game_stats.ships_left-= 1
            self._reset_level()
            
            sleep(0.5)
        else:
            self.game_active = False
            self.deactivate_play_button = False

    def _reset_level(self):
        """Resets the everything in the current level
        """
        self.ship.arsenal.arsenal.empty()
        self.alien_fleet.fleet.empty()
        self.alien_fleet.create_fleet()

    def restart_game(self) -> None:
        """Restarts the whole game from level 1
        """
        self.deactivate_play_button = True
        self.settings.initialize_dynamic_settings()
        self.game_stats.reset_stats()
        self.HUD.update_scores()
        self.HUD.update_level()
        self._reset_level()
        self.ship._center_ship()
        self.game_active = True
        pygame.mouse.set_visible(False)

    def _update_screen(self) -> None:
        """Displays all ships and background and a play button when not playing"""
        self.screen.blit(self.bg, (0,0))
        self.ship.draw()
        self.alien_fleet.draw()
        self.HUD.draw()

        if not self.game_active and not self.deactivate_play_button:
            self.play_button.draw()
            pygame.mouse.set_visible(True)
        
        pygame.display.flip()

    def _check_events(self) -> None:
        """Allows to quit the game and checks the status of the key pressed"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.game_stats.save_scores()
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and self.game_active == True:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._check_button_clicked()

    def _check_button_clicked(self):
        """ Verifies that the mouse is clicking on the play button
        """
        mouse_pos = pygame.mouse.get_pos()
        if self.play_button.check_clicked(mouse_pos) and not self.deactivate_play_button:
            self.restart_game()


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
            self.game_stats.save_scores()
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
