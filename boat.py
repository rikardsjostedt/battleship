import pygame

class Boat:

    def __init__(self, cells, game):
        self.cells = cells
        self.game = game
        self.alive = True

    def check(self, x , y, boat):
        for cell in self.cells:
            if cell.occupied:
                return False

        return True

    def place(self):
        for cell in self.cells:
            cell.occupied = True
            cell.parent = self

    def check_if_alive(self):
        for cell in self.cells:
            if not cell.hit:
                return True
        return False
