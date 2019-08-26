from board import Board


class Player:
    def __init__(self, game):
        self.id = id
        self.board = Board(game.amount_of_cols, game.window)

    def create_board(self):
        self.board.create_cells()
