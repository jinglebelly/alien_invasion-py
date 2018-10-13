import pygame
import sys
from pygame.sprite import Sprite
from random import randint
from pygame.sprite import Group
def run():
    pygame.init()
    screen=pygame.display.set_mode((500,500))

    class Bullet(Sprite):
        def __init__(self,screen):
            super(Bullet, self).__init__()
            self.screen = screen
            # 在(0,0)处创建一个表示子弹的矩形，再设置正确的位置
            self.rect = pygame.Rect(0, 0, 10,10)
            self.rect.x = randint(0,500)
            self.color = 60, 60, 60


        def update(self):
            """向上移动子弹"""
            # 更新表示子弹位置的小数值
            self.rect.y -= 1

        def draw_bullet(self):
            """在屏幕上绘制子弹"""
            pygame.draw.rect(self.screen, self.color, self.rect)

    bullets = Group()
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit()
        screen.fill((200, 200, 200))


        pygame.display.flip()

        for bullet in bullets.sprites():
            bullet = Bullet()

            bullet.draw_bullet()

run()