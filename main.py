import pygame
from pygame.locals import *


'''
main class - game logic
ships class - refrence board 
player class - spelare innehåller en board och X antal ships
board class - innehåller rutnät av X antal cells
cell class - en ruta i spelbrädet

'''
from board import Board
from game import Game

def main():
    (width, height) = (600, 800)
    game_running = True
    pygame.init()
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("BATTLESHIP 1337")
    background_color = (255, 255, 255)
    window.fill(background_color)

    game = Game(window)

    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.check_cell(event.pos)
                pygame.display.flip()
            if event.type == pygame.QUIT:
                pygame.quit()
                game_running = False


main()