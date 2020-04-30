import pygame
import random
from enum import Enum
from direction import Direction
pygame.init()
pygame.mixer.init()



class Tank:

    def __init__(self, x, y, speed, color, d_right=pygame.K_RIGHT, d_left=pygame.K_LEFT, d_up=pygame.K_UP,
                 d_down=pygame.K_DOWN, fire_key=pygame.K_RETURN):

        self.fire_key = fire_key
        self.recharge = False
        self.recharge_duration = 2 # in sec
        self.recharge_time = 0 # in sec

        self.lifes = 3
        self.x = x
        self.y = y
        self.speed = speed
        self.color = color
        self.width = 40
        self.height = 40
        self.direction = Direction.RIGHT

        self.KEY = {
            d_right: Direction.RIGHT,
            d_left: Direction.LEFT,
            d_up: Direction.UP,
            d_down: Direction.DOWN
        }

    def draw(self, screen, size_w, size_h):
        tank_c = (self.x + int(self.width / 2), self.y + int(self.height / 2))

        if self.x <= 0:
            self.x = size_w - self.width
        if self.y <= 0:
            self.y = size_h - self.height
        if self.x + self.width > size_w:
            self.x = 0
        if self.y >= size_h:
            self.y = 0

        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 2)
        pygame.draw.circle(screen, self.color, tank_c, int(self.width / 2))

        if self.direction == Direction.RIGHT:
            pygame.draw.line(screen, self.color, tank_c,
                             (self.x + self.height + int(self.height / 2), int(self.y + self.width / 2)), 4)
        if self.direction == Direction.LEFT:
            pygame.draw.line(screen, self.color, tank_c,
                             (self.x - self.height + int(self.height / 2), self.y + int(self.width / 2)), 4)
        if self.direction == Direction.UP:
            pygame.draw.line(screen, self.color, tank_c, (self.x + int(self.height / 2), self.y - int(self.width / 2)),
                             4)
        if self.direction == Direction.DOWN:
            pygame.draw.line(screen, self.color, tank_c,
                             (self.x + int(self.height / 2), self.y + self.width + int(self.width / 2)), 4)

    def change_direction(self, direction):
        self.direction = direction

    def move(self, seconds):
        if self.direction == Direction.LEFT:
            self.x -= int(self.speed * seconds)
        if self.direction == Direction.RIGHT:
            self.x += int(self.speed * seconds)
        if self.direction == Direction.UP:
            self.y -= int(self.speed * seconds)
        if self.direction == Direction.DOWN:
            self.y += int(self.speed * seconds)

        self.recharge_time += seconds
        if self.recharge_time >= self.recharge_duration:
            self.recharge = False
            self.recharge_time = 0
