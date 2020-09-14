import pygame

class Alien_ship(): 
	def __init__(self, screen):
		self.screen = screen 
		self.image = pygame.image.load('images/Alien_ship.png')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		# All new invasion will start from bottom
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
	def blitme(self):
		self.screen.blit(self.image, self.rect)