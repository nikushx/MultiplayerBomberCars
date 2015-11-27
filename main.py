import pygame, math, sys
import Car
import Wall
from pygame.locals import *
screen = pygame.display.set_mode((1024,768))
clock = pygame.time.Clock()

#Get Screen Size
screen_size = screen.get_rect()

#Set Spawn of Cars
center_position = screen_size.center
x, y = center_position
car_one_position = x - 75, y
car_two_position = x + 75, y
car_one = Car.CarSprite('car_one.png', car_one_position)
car_two = Car.CarSprite('car_two.png', car_two_position)
car_group = pygame.sprite.RenderPlain(car_one, car_two)

#Set Spawn of Wall
walls = [
    Wall.WallSprite((25,25)),
    Wall.WallSprite((75,25)),
    Wall.WallSprite((125,25)),
    Wall.WallSprite((175,25)),
]
wall_group = pygame.sprite.RenderPlain(walls)

#Loop
while 1:

    #Set FPS
    deltat = clock.tick(60)
    car_group.update(deltat)

    #Car Collision
    Car.CheckCollision(car_one, car_two)

    #User Input
    Car.CarMovement(car_one, car_two)

    #Render Screen
    screen.fill((0,0,0))
    wall_group.draw(screen)
    car_group.draw(screen)

    #Display Game
    pygame.display.flip()