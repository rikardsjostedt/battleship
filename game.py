from player import Player
from time import sleep
import pygame

class Game:
    current_gamestate = "setup"

    def __init__(self, window):
        self.window = window
        self.amount_of_cols = 6
        self.player1 = Player(self, 1)
        self.player2 = Player(self, 2)
        self.current_player = self.player1
        self.current_board = self.player1.board
        self.setup_game()

    def setup_game(self):
        self.current_player.board.render()

    def get_amount_of_cols(self):
        return self.amount_of_cols

    def run_game(self):
        print("starta")

    def event_handler(self, event):
        hit = self.current_player.board.check_cell(event.pos)
        self.current_player.board.render()
        if hit & (self.current_gamestate == "running"):
            sleep(1)
            self.change_current_player()

    def change_current_player(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            if self.current_gamestate == "setup":
                self.current_gamestate = "running"
            self.current_player = self.player1
        self.current_player.board.render()

    def show_boat(self, event):
        px, py = event.pos
        size = self.current_player.board.cell_size
        x = int(px/size)
        y = int(py/size)
        if (x < self.amount_of_cols) & (y < self.amount_of_cols - 2):
            self.current_player.board.render()
            #pygame.display.update()
            pygame.draw.rect(self.window, (0, 0, 0), (x * size, y * size, size, size * 3))
            print(x, y)
