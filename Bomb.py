import pygame, math, ctypes
from pygame.locals import *

#Bomb Sprite Class
class BombSprite(pygame.sprite.Sprite):

    def __init__(self, image, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.rect = pygame.Rect(self.image.get_rect())
        self.rect.center = position

    #def update(self, deltat):

