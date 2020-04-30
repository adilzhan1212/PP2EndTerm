import pygame
import random
from enum import Enum
from tank import Tank
from direction import Direction
from bullet import Bullet

pygame.init()
pygame.mixer.init()

size_w = 1600
size_h = 900
screen = pygame.display.set_mode((size_w, size_h))
background = pygame.image.load("background.jpg").convert()
background = pygame.transform.scale(background, (size_w, size_h))
FPS = 60
clock = pygame.time.Clock()

sound_hit = pygame.mixer.Sound('sound_hit.wav')

run = True
tank_1 = Tank(300, 300, 200, (255, 0, 0))
tank_2 = Tank(100, 100, 200, (100, 230, 40), pygame.K_d, pygame.K_a, pygame.K_w, pygame.K_s, pygame.K_SPACE)

tanks = [tank_1, tank_2]
bullets = []

def hit_check(bullet, which_bullet):
    global tanks

    shadow_x1 = []
    shadow_x2 = []
    shadow_y1 = []
    shadow_y2 = []
    i = 0
    for tank in tanks:
        shadow_x1.append(tank.x)
        shadow_x2.append(tank.x + tank.width)
        shadow_y1.append(tank.y)
        shadow_y2.append(tank.y + tank.height)

        if shadow_x1[i] <= bullet.x <= shadow_x2[i] and shadow_y1[i] <= bullet.y <= shadow_y2[i]:
            sound_hit.play()

            tank.lifes -= 1
            if tank.lifes <= 0: del tanks[i]
            del bullets[which_bullet]

        i += 1


while run:
    millis = clock.tick(FPS)
    seconds = millis / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

            for tank in tanks:
                if event.key in tank.KEY.keys():
                    tank.change_direction(tank.KEY[event.key])
                if event.key == tank.fire_key:
                    if tank.recharge != True:
                        bullets.append(Bullet(tank, screen))
                        tank.recharge = True

    screen.blit(background, (0, 0))

    for tank in tanks:

        tank.move(seconds)
        tank.draw(screen, size_w, size_h)

    i = 0
    for bullet in bullets:
        hit_check(bullet, i)
        bullet.move(seconds)
        bullet.draw()
        if bullet.life_time >= bullet.del_time: del bullets[i]
        i += 1

    print(seconds)
    pygame.display.flip()

pygame.quit()
