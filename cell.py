import pygame
from random import randrange

class Cell:
    '''
    En cell med x,y värde samt occupied vilket indikerar om den exempelvis har ett skepp på sig
    '''
    def __init__(self, x, y, window, cell_size):
        self.x = x
        self.y = y
        self.window = window
        self.cell_size = cell_size
        self.px = x * cell_size
        self.py = y * cell_size
        self.free = True
        self.occupied = False


    def render(self):
        font = pygame.font.SysFont('Comic Sans MS', 30)
        coords = str(self.x) + ", " + str(self.y)
        text = font.render(coords, False, (255, 255, 255))
        pygame.draw.rect(self.window, (randrange(250), 0, 0), (self.px, self.py, self.cell_size, self.cell_size))
        self.window.blit(text, (self.px, self.py))



