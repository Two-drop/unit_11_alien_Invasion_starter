"""hud.py
author: Noah Kattner
date: 04/18/2025"""

import json

from typing import TYPE_CHECKING
if TYPE_CHECKING:
     from Lab14_nkattner_1 import AlienInvasion


class GameStats():
    """ Controls the data for the game
    """
    def __init__(self, game: 'AlienInvasion'):
        """ Initializes the score and level settings for the game

        Arguments:
            game -- References the AlienInvasion game's main file
        """
        self.game = game
        self.settings = game.settings
        self.max_score = 0
        self.init_saved_scores()
        self.reset_stats()
    
    def init_saved_scores(self) -> None:
        """ Initializes the settings to save the hi score into a json file
        """
        self.path = self.settings.scores_file
        if self.path.exists() and self.path.stat.__sizeof__() > 20:
            contents = self.path.read_text()
            scores = json.loads(contents)
            self.hi_score = scores.get('hi_score', 0)
        else:
            self.hi_score = 0
            self.save_scores()
    
    def save_scores(self) -> None:
        """Saves the new hi score into the json file
        """
        scores = {
            'hi_score': self.hi_score
        }
        contents = json.dumps(scores, indent=4)
        try:
            self.path.write_text(contents)
        except FileNotFoundError as e:
            print(f'File Not Found: {e}')

    def reset_stats(self) -> None:
        """ Resets the the game upon complete death
        """
        self.ships_left = self.settings.starting_ship_count
        self.score = 0
        self.level = 1
    
    def update(self, collisions) -> None:
        """ Updates the max and base score

        Arguments:
            collisions -- takes in the collision between alien ship and bullet.
        """
        self._update_score(collisions)


        self._update_max_score()

        self._update_hi_score()

    def _update_max_score(self) -> None:
        """ Updated the player's max score
        """
        if self.score > self.max_score:
            self.max_score = self.score
    
    def _update_hi_score(self) -> None:
        """ Updated the player's hi score
        """
        if self.score > self.hi_score:
            self.hi_score = self.score
        
    def _update_score(self, collisions) -> None:
        """ Updated the base score of the player

        Arguments:
            collisions -- takes in the collision between alien ship and bullet
        """
        for alien in collisions.values():
            self.score += self.settings.alien_points
        print(f'Basic: {self.score}')
    
    def update_level(self) -> None:
        """ Updated the current level upon completion
        """
        self.level += 1