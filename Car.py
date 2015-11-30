import pygame, math, ctypes
from pygame.locals import *

#Car Sprite Class
class CarSprite(pygame.sprite.Sprite):
    MAX_FORWARD_SPEED = 15
    MAX_REVERSE_SPEED = 10

    def __init__(self, image, position):
        pygame.sprite.Sprite.__init__(self)
        self.src_image = pygame.image.load(image)
        self.position = position
        self.speed = self.direction = 0
        self.k_left = self.k_right = self.k_down = self.k_up = 0



    def update(self, deltat):
        #Simulation
        self.speed += (self.k_up + self.k_down)
        if self.speed > self.MAX_FORWARD_SPEED:
            self.speed = self.MAX_FORWARD_SPEED
        if self.speed < -self.MAX_REVERSE_SPEED:
            self.speed = -self.MAX_REVERSE_SPEED
        self.direction += (self.k_left + self.k_right)
        x, y = self.position
        rad = self.direction * math.pi / 180
        x += -self.speed*math.sin(rad)
        y += -self.speed*math.cos(rad)
        self.position = (x, y)
        self.image = pygame.transform.rotate(self.src_image, self.direction)
        self.rect = self.image.get_rect()
        self.rect.center = self.position

def CarMovement(car, car2):

    #User input
    for event in pygame.event.get():
        if not hasattr(event, 'key'): continue
        down = event.type == KEYDOWN
        if event.key == K_ESCAPE: sys.exit(0)
        #Car 1
        if event.key == K_UP: car.k_up = down * 2
        elif event.key == K_DOWN: car.k_down = down * -2
        if event.key == K_RIGHT: car.k_right = down * -5
        if event.key == K_LEFT: car.k_left = down * 5
        #Car 2
        if event.key == K_w: car2.k_up = down * 2
        elif event.key == K_s: car2.k_down = down * -2
        if event.key == K_d: car2.k_right = down * -5
        if event.key == K_a: car2.k_left = down * 5
    if (car.speed != 0):
        if car.speed > 0: car.speed -= 0.5
        elif car.speed < 0: car.speed += 0.5
    if (car2.speed != 0):
        if car2.speed > 0: car2.speed -= 0.5
        elif car2.speed < 0: car2.speed += 0.5

def CheckCollision(car1, car2, walls, safe_position_1, safe_position_2):
    car_collide = pygame.sprite.collide_rect(car1, car2)
    hit1 = False
    hit2 = False
    for wall in walls:
        wall_collide_1 = pygame.sprite.collide_rect(car1, wall)
        if wall_collide_1: hit1 = True
        wall_collide_2 = pygame.sprite.collide_rect(car2, wall)
        if wall_collide_2: hit2 = True
    if car_collide: print "Car Collision"
    if hit1 == False: safe_position_1 = car1.position
    if hit1 == True:
        car1.position = safe_position_1
    if hit2 == False: safe_position_2 = car2.position
    if hit2 == True:
        car2.position = safe_position_2
    return (safe_position_1, safe_position_2)
