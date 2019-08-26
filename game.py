from player import Player


class Game:
    def __init__(self, window):
        self.window = window
        self.amount_of_cols = 6

        self.player1 = Player(self)
        self.player2 = Player(self)
        self.setup_game()

    def setup_game(self):
        self.player1.create_board()
        self.player2.create_board()

    def get_amount_of_cols(self):
        return self.amount_of_cols
