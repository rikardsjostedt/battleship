from board import Board


class Player:
    def __init__(self, game, id):
        self.id = id
        self.board = Board(game, id)


