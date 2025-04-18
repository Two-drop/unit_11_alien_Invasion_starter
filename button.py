"""button.py
author: Noah Kattner
date: 04/18/2025"""

import pygame.font

from typing import TYPE_CHECKING
if TYPE_CHECKING:
     from Lab14_nkattner_1 import AlienInvasion

class Button:
    """Class to handle information about the play button
    """

    def __init__(self, game: 'AlienInvasion', msg) -> None:
        """Initializes all settings related to the play button

        Arguments:
            game -- References the AlienInvasion game's main file
            msg -- Parameter to take in a text to display as message
        """
        self.game = game
        self.screen = game.screen
        self.boundaries = game.screen.get_rect()
        self.settings = game.settings
        self.font = pygame.font.Font(self.settings.font_file, 
                    self.settings.button_font_size)
        
        self.rect = pygame.Rect(self.settings.button_left_offset, 
                    self.settings.button_top_offset, self.settings.button_w,
                    self.settings.button_h)
        self.center = self.boundaries.center
        self._prep_msg(msg)


    def _prep_msg(self, msg) -> None:
        """Function to position and load the message to be displayed

        Arguments:
            msg -- takes in the message that we want to display
        """
        self.msg_image = self.font.render(msg, True, self.settings.text_color, None)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.center

    
    def draw(self) -> None:
        """Draws the message and the button onto the screen
        """
        self.screen.fill(self.settings.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    
    def check_clicked(self, mouse_pos) -> bool:
        """Function to check is our mouse is clicking on the button

        Arguments:
            mouse_pos -- Takes in the position of mouse

        Returns:
            returns true if the mouse is clicking on the button
        """
        return self.rect.collidepoint(mouse_pos)