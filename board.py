from cell import Cell
class Board:

    def __init__(self, amount_of_cols):
        self.amount_of_cols = amount_of_cols
        print(self.amount_of_cols)
        self.cells = []
        self.create_cells()
        print(self.cells)

    def create_cells(self):
        #broken af
        print(range(self.amount_of_cols - 1))
        for i in range(self.amount_of_cols - 1):
            tempList = []
            for j in range(self.amount_of_cols - 1):
                tempList[0] = j #Cell(i, j)
                print(tempList)
            self.cells[i].append(tempList)







