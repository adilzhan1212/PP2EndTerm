import pygame
import random
from enum import Enum
from tank import Tank
from direction import Direction
pygame.init()
pygame.mixer.init()

sound_shoot = pygame.mixer.Sound('sound_shoot.wav')





class Bullet:

    def __init__(self, tank, screen):
        sound_shoot.play()
        self.screen = screen
        self.size = 8
        self.tank = tank
        self.color = tank.color
        self.direction = tank.direction
        self.speed = 500
        self.life_time = 0
        self.del_time = 1.5 # in sec
        if tank.direction == Direction.RIGHT:
            self.x = tank.x + tank.height + int(tank.height / 2)
            self.y = int(tank.y + tank.width / 2)
        if self.direction == Direction.LEFT:
            self.x = tank.x - tank.height + int(tank.height / 2)
            self.y = tank.y + int(tank.width / 2)
        if self.direction == Direction.UP:
            self.x = tank.x + int(tank.height / 2)
            self.y = tank.y - int(tank.width / 2)
        if self.direction == Direction.DOWN:
            self.x = tank.x + int(tank.height / 2)
            self.y = tank.y + tank.width + int(tank.width / 2)

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.size)

    def move(self, seconds):
        self.life_time += seconds

        if self.direction == Direction.RIGHT:
            self.x += int(self.speed * seconds)
        if self.direction == Direction.LEFT:
            self.x -= int(self.speed * seconds)
        if self.direction == Direction.UP:
            self.y -= int(self.speed * seconds)
        if self.direction == Direction.DOWN:
            self.y += int(self.speed * seconds)




