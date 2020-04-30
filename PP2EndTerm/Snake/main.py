import pygame

from snake import Snake
from fruit import Fruit

pygame.init()
screen_size = 900
screen = pygame.display.set_mode((screen_size, screen_size))

run = True

cells_amount = 30
cell_size = 900 / cells_amount
cell_x = []
cell_y = []

j = 0
for i in range(0, cells_amount + 1):
    cell_x.append(j)
    cell_y.append(j)
    j += cell_size


def gameSpace(cells_amount, cell_size, cell_x, cell_y, screen, screen_size):
    for i in range(0, cells_amount + 1):
        pygame.draw.line(screen, (255, 255, 255), (int(cell_x[i]), 0), (int(cell_x[i]), screen_size))
    for i in range(0, cells_amount + 1):
        pygame.draw.line(screen, (255, 255, 255), (0, int(cell_x[i])), (screen_size, int(cell_x[i])))

def eat_check(fruit, snake):
    if fruit.x + snake.cell_size/2 == snake.elements[0][0] + snake.cell_size/2 and fruit.y + snake.cell_size/2 == snake.elements[0][1] + snake.cell_size/2:
        return True
    return False

clock = pygame.time.Clock()
FPS = 15

snake = Snake(cells_amount, cell_size, cell_x, cell_y,screen_size)

fruit = Fruit(snake)

while run:
    millis = clock.tick(FPS)
    seconds = millis / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_d and (snake.direction_x != -1 or len(snake.elements) == 1):
                snake.direction_x = 1
                snake.direction_y = 0
            if event.key == pygame.K_a and (snake.direction_x != 1 or len(snake.elements) == 1):
                snake.direction_x = -1
                snake.direction_y = 0
            if event.key == pygame.K_w and (snake.direction_y != 1 or len(snake.elements) == 1):
                snake.direction_x = 0
                snake.direction_y = -1
            if event.key == pygame.K_s and (snake.direction_y != -1 or len(snake.elements) == 1):
                snake.direction_x = 0
                snake.direction_y = 1



    grow = eat_check(fruit,snake)
    if grow:
        snake.is_add = True
        fruit = Fruit(snake)

    screen.fill((0, 0, 0))
    gameSpace(cells_amount, cell_size, cell_x, cell_y, screen, screen_size)

    fruit.draw(screen, snake)

    snake.move()
    snake.draw(screen)

    if snake.collision(screen):
        run = False
    pygame.display.flip()

pygame.quit()