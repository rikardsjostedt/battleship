from cell import Cell
import pygame
class Board:

    def __init__(self, amount_of_cols, window):
        self.window = window
        self.amount_of_cols = amount_of_cols
        self.cells = []
        self.cell_size = pygame.display.get_surface().get_width() / amount_of_cols
        self.create_cells() # skapa celler

    def create_cells(self):
        for i in range(self.amount_of_cols):
            tempList = []
            for j in range(self.amount_of_cols):
                cell = Cell(i, j, self.window, self.cell_size)
                tempList.append(cell)
            self.cells.append(tempList)

    def render(self):
        for list in self.cells:
            for cell in list:
                cell.render()
        pygame.display.flip()

    def check_cell(self, pos):
        px, py = pos
        x = int(px / self.cell_size)
        y = int(py / self.cell_size)
        self.cells[x][y].trigger_click()






