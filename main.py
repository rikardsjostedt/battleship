import pygame
from pygame.locals import *
from time import sleep


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
            if (event.type == pygame.MOUSEMOTION) & (game.current_gamestate == "setup"):
                game.show_boat(event)
                pygame.display.flip()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if y <= width:
                    game.event_handler(event)
                    pygame.display.flip()
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_LEFT) & (game.current_gamestate == "setup"):
                    game.change_current_player()
            if event.type == pygame.QUIT:
                pygame.quit()
                game_running = False


main()