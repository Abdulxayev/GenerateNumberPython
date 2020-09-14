import sys

import pygame 

from settings import Settings 
from ship import Alien_ship
import game_functions as gf

def runGame():
	# Creating game objects "Window"
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	# screen = pygame.display.set_mode((1200, 800)) 
	pygame.display.set_caption("Alien Invasion By Benjamin")
	# screen settings

	ship = Alien_ship(screen)
	screen.fill(ai_settings.bg_color)
	# bg_color = (230, 230, 230)

	ship.blitme()

	while True:
		# Events Mouse, Keyboard 
		gf.check_events()
		gf.update_screen(ai_settings, screen, ship)


		pygame.display.flip()


runGame();