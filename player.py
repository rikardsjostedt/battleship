from board import Board
from boat import Boat


class Player:
    def __init__(self, game, id):
        self.id = id
        self.board = Board(game, id)
        self.boats = []


