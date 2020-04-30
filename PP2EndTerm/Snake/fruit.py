import pygame
from random import randrange as rand


class Fruit:
    color = (255, 0, 0)

    def __init__(self, snake):
        self.pos = self.generate(snake)
        self.x = self.pos[0]
        self.y = self.pos[1]

    def generate(self, snake):
        ok = False
        while not ok:
            ok = True
            x = rand(int(snake.cell_size), int(snake.screen_size - snake.cell_size), int(snake.cell_size))
            y = rand(int(snake.cell_size), int(snake.screen_size - snake.cell_size), int(snake.cell_size))
            for element in snake.elements:
                if x == element[0] and y == element[1]:
                    ok = False
                    break
        pos = []
        pos.append(x)
        pos.append(y)
        return pos

    def draw(self, screen, snake):
        pygame.draw.rect(screen, self.color, (int(self.x)+1, int(self.y)+1, int(snake.cell_size)-1, int(snake.cell_size)-1))
