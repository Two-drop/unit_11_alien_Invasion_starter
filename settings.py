"""settings.py
date: 04/03/2025"""

from pathlib import Path

class Settings:
     """Class to store settings to be used in other files."""
     def __init__(self) -> None:
          """Initialize game settings"""
          self.name: str = 'Alien Invasion'
          self.screen_w = 1200
          self.screen_h = 800
          self.FPS = 60
          self.bg_file = Path.cwd() / 'Assets' / 'images' / 'Starbasesnow.png'
          self.difficulty_scale = 1.1

          self.ship_file = Path.cwd() / 'Assets' / 'images' / 'ship2(no bg).png'
          self.ship_w = 40
          self.ship_h = 60

          self.bullet_file = Path.cwd() / 'Assets' / 'images' / 'laserBlast.png'
          self.laser_sound = Path.cwd() / 'Assets' / 'sound' / 'laser.mp3'
          self.impact_sound = Path.cwd() / 'Assets' / 'sound' / 'impactSound.mp3'

          self.alien_file = Path.cwd() / 'Assets' / 'images' / 'enemy_4.png'
          self.alien_w = 40
          self.alien_h = 40
          self.fleet_direction = 1

          self.button_w = 200
          self.button_h = 50
          self.button_left_offset = (self.screen_w-self.button_w)//2
          self.button_top_offset = (self.screen_h-self.button_h)//2
          self.button_color = (0, 135, 50)

          self.text_color = (255, 255, 255)
          self.button_font_size = 48
          self.HUD_font_size = 20
          self.font_file = Path.cwd() / 'Assets' / 'Fonts' / 'Silkscreen' / 'Silkscreen-Bold.ttf'

     def initialize_dynamic_settings(self) -> None:
          self.ship_speed = 5
          self.starting_ship_count = 3

          self.bullet_speed = 9
          self.bullet_w = 25
          self.bullet_h = 80
          self.bullet_amount = 5

          self.fleet_speed = 3
          self.fleet_drop_speed = 20
     
     def increase_difficulty(self) -> None:
          self.ship_speed *= self.difficulty_scale
          self.bullet_speed *= self.difficulty_scale
          self.fleet_speed *= self.difficulty_scale