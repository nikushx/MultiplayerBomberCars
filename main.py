import pygame, math, sys
import Car
import Wall
from pygame.locals import *
screen = pygame.display.set_mode((1050,750))
clock = pygame.time.Clock()

#Get Screen Size
screen_size = screen.get_rect()

#Set Spawn of Cars
center_position = screen_size.center
x, y = center_position
car_one_position = x - 75, y
car_two_position = x + 75, y
car_one = Car.CarSprite('car_one.png', car_one_position)
safe_position_1 = 0, 0
car_two = Car.CarSprite('car_two.png', car_two_position)
safe_position_2 = 0, 0
car_group = pygame.sprite.RenderPlain(car_one, car_two)

#Set Spawn of Wall
walls = [
    #Left Vertical
    Wall.WallSprite((25,75)),
    Wall.WallSprite((25,125)),
    Wall.WallSprite((25,175)),
    Wall.WallSprite((25,225)),
    Wall.WallSprite((25,275)),
    Wall.WallSprite((25,325)),
    Wall.WallSprite((25,375)),
    Wall.WallSprite((25,425)),
    Wall.WallSprite((25,475)),
    Wall.WallSprite((25,525)),
    Wall.WallSprite((25,575)),
    Wall.WallSprite((25,625)),
    Wall.WallSprite((25,675)),
    #Top Horizontal
    Wall.WallSprite((75,25)),
    Wall.WallSprite((125,25)),
    Wall.WallSprite((175,25)),
    Wall.WallSprite((225,25)),
    Wall.WallSprite((275,25)),
    Wall.WallSprite((325,25)),
    Wall.WallSprite((375,25)),
    Wall.WallSprite((425,25)),
    Wall.WallSprite((475,25)),
    Wall.WallSprite((525,25)),
    Wall.WallSprite((575,25)),
    Wall.WallSprite((625,25)),
    Wall.WallSprite((675,25)),
    Wall.WallSprite((725,25)),
    Wall.WallSprite((775,25)),
    Wall.WallSprite((825,25)),
    Wall.WallSprite((875,25)),
    Wall.WallSprite((925,25)),
    Wall.WallSprite((975,25)),
    #Right Vertical
    Wall.WallSprite((1025,75)),
    Wall.WallSprite((1025,125)),
    Wall.WallSprite((1025,175)),
    Wall.WallSprite((1025,225)),
    Wall.WallSprite((1025,275)),
    Wall.WallSprite((1025,325)),
    Wall.WallSprite((1025,375)),
    Wall.WallSprite((1025,425)),
    Wall.WallSprite((1025,475)),
    Wall.WallSprite((1025,525)),
    Wall.WallSprite((1025,575)),
    Wall.WallSprite((1025,625)),
    Wall.WallSprite((1025,675)),
    #Bottom Horizontal
    Wall.WallSprite((75,725)),
    Wall.WallSprite((125,725)),
    Wall.WallSprite((175,725)),
    Wall.WallSprite((225,725)),
    Wall.WallSprite((275,725)),
    Wall.WallSprite((325,725)),
    Wall.WallSprite((375,725)),
    Wall.WallSprite((425,725)),
    Wall.WallSprite((475,725)),
    Wall.WallSprite((525,725)),
    Wall.WallSprite((575,725)),
    Wall.WallSprite((625,725)),
    Wall.WallSprite((675,725)),
    Wall.WallSprite((725,725)),
    Wall.WallSprite((775,725)),
    Wall.WallSprite((825,725)),
    Wall.WallSprite((875,725)),
    Wall.WallSprite((925,725)),
    Wall.WallSprite((975,725)),
]
wall_group = pygame.sprite.RenderPlain(walls)

#Loop
while 1:

    #Set FPS
    deltat = clock.tick(60)
    car_group.update(deltat)

    #Car Collision
    safe_position_1, safe_position_2 = Car.CheckCollision(car_one, car_two, walls, safe_position_1, safe_position_2)

    #User Input
    Car.CarMovement(car_one, car_two)

    #Render Screen
    screen.fill((0,0,0))
    wall_group.draw(screen)
    car_group.draw(screen)

    #Display Game
    pygame.display.flip()