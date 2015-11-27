import pygame, math, ctypes
from pygame.locals import *

#Wall Sprite Class
class WallSprite(pygame.sprite.Sprite):
    wall_pic = pygame.image.load('wall.gif')
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = self.wall_pic
        self.rect = pygame.Rect(self.wall_pic.get_rect())
        self.rect.center = position