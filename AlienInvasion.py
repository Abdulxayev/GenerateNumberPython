import sys

import pygame 
def runGame():
	# Creating game objects "Window"
	pygame.init()
	screen = pygame.display.set_mode((1200, 800)) 
	pygame.display.set_caption("Alien Invasion By Benjamin")
	# screen settings
	bg_color = (230, 230, 230)

	while True:
		# Events Mouse, Keyboard 
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()


		pygame.display.flip()


runGame();