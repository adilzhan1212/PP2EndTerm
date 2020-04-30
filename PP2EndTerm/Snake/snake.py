import pygame
pygame.init()


class Snake:

    def __init__(self,cells_amount, cell_size, cell_x, cell_y, screen_size):
        self.cells_amount = cells_amount
        self.cell_size = cell_size
        self.cell_x = cell_x
        self.cell_y = cell_y
        self.screen_size = screen_size
        self.direction_x = 1
        self.direction_y = 0

        self.is_add = False

        self.size = 1
        self.elements = [[self.cell_x[5], self.cell_y[5]]]



    def move(self):

        if self.is_add:
            self.size += 1
            self.elements.append([0, 0])
            self.is_add = False
        for i in range(self.size - 1, 0, -1):
            self.elements[i][0] = self.elements[i - 1][0]
            self.elements[i][1] = self.elements[i - 1][1]


        self.elements[0][0] += self.cell_size * self.direction_x
        self.elements[0][1] += self.cell_size * self.direction_y



    def draw(self, screen):


        for element in self.elements:
            x = element[0]
            y = element[1]

            pygame.draw.rect(screen, (0, 255, 0), (int(x)+1, int(y)+1, int(self.cell_size)-1, int(self.cell_size)-1))


    def collision(self, screen):
        col = False
        for i in range(1, len(self.elements)):
            if self.elements[0][0] == self.elements[i][0] and self.elements[0][1] == self.elements[i][1]:
                col = True
        if col:
            pygame.font.init()
            font = pygame.font.SysFont("Arial", 36)
            text = font.render("Game over", 1, (255, 255, 255))
            place = text.get_rect(center=(self.screen_size // 2, self.screen_size // 2))
            font2= pygame.font.SysFont("Arial", 18)
            text2 = font2.render("Score: {}".format(self.size), 1, (255,255,255))
            place2 = text2.get_rect(center=(self.screen_size//2, self.screen_size//2 + 30))
            screen.blit(text2, place2)
            screen.blit(text, place)
            pygame.display.flip()
            pygame.time.delay(2000)
            return True

        return False