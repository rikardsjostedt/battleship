from cell import Cell
import pygame


class Board:

    def __init__(self, game, id):
        self.game = game
        self.window = game.window
        self.amount_of_cols = game.amount_of_cols
        self.id = id
        self.boats = []
        self.cells = []
        self.cell_size = pygame.display.get_surface().get_width() / game.amount_of_cols
        self.create_cells() # skapa celler

    def create_cells(self):
        for i in range(self.amount_of_cols):
            tempList = []
            for j in range(self.amount_of_cols):
                cell = Cell(i, j, self.window, self.cell_size, self.game)
                tempList.append(cell)
            self.cells.append(tempList)

    def render(self):
        self.window.fill([255,255,255])
        for list in self.cells:
            for cell in list:
                cell.render()
        font = pygame.font.SysFont('Comic Sans MS', 30)
        if self.game.current_gamestate == "setup":
            player_area_text = "Spelare " + str(self.game.current_player.id)
        else:
            if self.game.current_player.id == 1:
                player_area_text = "Spelare " + str(2)
            else:
                player_area_text = "Spelare " + str(1)
        text = font.render(player_area_text, False, (0, 0, 0))
        w, h = pygame.display.get_surface().get_size()
        text_rect = text.get_rect(center=(w/2, w + ((h-w)/2)))
        self.window.blit(text, text_rect)
        pygame.display.flip()

    def check_cell(self, pos, boat=None):
        px, py = pos
        #print(boat)
        x = int(px / self.cell_size)
        y = int(py / self.cell_size)
        if self.game.current_gamestate == "setup":
            return boat.check(x, y, boat)
        else:
            return self.cells[x][y].trigger_click()

    def render_winner_text(self, player):
        font = pygame.font.SysFont('Comic Sans MS', 30)
        self.window.fill([255, 255, 255])
        winner_text = "Spelare " + str(player.id) + " vinner!"
        text = font.render(winner_text, False, (0, 0, 0))
        w, h = pygame.display.get_surface().get_size()
        text_rect = text.get_rect(center=(w / 2, w + ((h - w) / 2)))
        self.window.blit(text, text_rect)
        pygame.display.flip()
