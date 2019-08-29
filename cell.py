import pygame
from random import randrange


class Cell:
    '''
    En cell med x,y värde samt occupied vilket indikerar om den exempelvis har ett skepp på sig
    '''
    def __init__(self, x, y, window, cell_size, game):
        self.game = game
        self.x = x
        self.y = y
        self.window = window
        self.cell_size = cell_size
        self.px = x * cell_size
        self.py = y * cell_size
        self.hit = False
        self.occupied = False
        self.parent = None

    def render(self):
        font = pygame.font.SysFont('Comic Sans MS', 30)
        coords = str(self.x) + ", " + str(self.y)
        text = font.render(coords, False, (255, 255, 255))
        if self.occupied & self.hit:
            pygame.draw.rect(self.window, (255, 0, 0), (self.px, self.py, self.cell_size, self.cell_size))
        elif self.hit:
            pygame.draw.rect(self.window, (255, 255, 255), (self.px, self.py, self.cell_size, self.cell_size))
        elif self.occupied & (self.game.current_gamestate == "setup"):
            pygame.draw.rect(self.window, (0, 0, 0), (self.px, self.py, self.cell_size, self.cell_size))
        else:
            pygame.draw.rect(self.window, (64, 244, 224), (self.px, self.py, self.cell_size, self.cell_size))

        self.window.blit(text, (self.px, self.py))

    def trigger_click(self):
        if self.game.current_gamestate == "setup":
            self.occupied = True

        elif self.game.current_gamestate == "running":
            if self.hit:
                return False
            elif (not self.hit) & self.occupied:
                self.hit = True
                self.render()
                if not self.parent.check_if_alive():
                    self.parent.alive = False
                return False
            else:
                self.hit = True
        self.render()
        return True

