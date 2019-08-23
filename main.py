import pygame
from pygame.locals import *


'''
main class - game logic
player class - spelare * 2
board class - spelbrädet * 2
cell class - en ruta i spelbrädet
'''
def main():
    (width, height) = (400, 400)
    game_running = True
    pygame.init()
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("BATTLESHIP 1337")
    pygame.display.flip()
    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                game_running = False



main()