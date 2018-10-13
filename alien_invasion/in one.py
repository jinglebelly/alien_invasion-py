import pygame
import sys
from pygame.sprite import Sprite
from pygame.sprite import Group
def run_game():
	pygame.init()
	screen=pygame.display.set_mode((1200,800))
	pygame.display.set_caption('Alien Invasion')

	image = pygame.image.load('images/ship.bmp')
	rect = image.get_rect()
	screen_rect = screen.get_rect()

	rect.centerx = screen_rect.centerx
	rect.bottom = screen_rect.bottom

	center = float(rect.centerx)
	moving_right = False
	moving_left = False
	bullets = Group()
	class Bullet(Sprite):
		def __init__(self):
			super().__init__()
			self.screen = screen
			self.rect = pygame.Rect(0, 0, 3,15)
			self.rect.centerx = rect.centerx
			self.rect.top = rect.top
			self.y = float(self.rect.y)
			self.color = 60, 60, 60
			self.speed_factor = 1
		def update(self):
			self.y -= self.speed_factor
			self.rect.y = self.y



	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					moving_right = True
				elif event.key == pygame.K_LEFT:
					moving_left = True
				elif event.key == pygame.K_SPACE:
					# if len(bullets) < 3:
						new_bullet = Bullet()
						bullets.add(new_bullet)
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_RIGHT:
					moving_right = False
				elif event.key == pygame.K_LEFT:
					moving_left = False
		if moving_right and rect.right < screen_rect.right:
			center += 1.5
		if moving_left and rect.left > screen_rect.left:
			center -= 1.5
		rect.centerx = center

		bullets.update()

		for bullet in bullets.copy():
			if bullet.rect.bottom <= 0:
				bullets.remove(bullet)

		'''print(len(bullets))'''
		screen.fill((230, 230, 230))

		for bullet in bullets.sprites():
			pygame.draw.rect(bullet.screen, bullet.color, bullet.rect)
		screen.blit(image, rect)
		pygame.display.flip()
	
run_game()
