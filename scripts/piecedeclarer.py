puzzlegrid = [[0, 0, 0, 0], 
              [0, 0, 0, 0], 
              [0, 0, 0, 0], 
              [0, 0, 0, 0]]
pieces = ['0001020312','0001021011','000102101112']

def piececounter(pcs,grid):
    count = 0
    for i in pcs:
        count += pcs[i].squares
    puzzlesize = sum([len(x) for x in grid])
    if count == puzzlesize:
        return True
    else:
        return False

class Piece:
    def __init__(self, shape,number):
        self.shape = shape
        self.number = number
        if len(self.shape) % 2 != 0:
            self.shape = self.shape[:-1]
        self.squares = len(self.shape) // 2

class Puzzle:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.columns = len(grid[0]) if self.rows > 0 else 0

Pieces = []
for i in pieces:
    piece = Piece(i, pieces.index(i))
    Pieces.append(piece)

Puzzlegrid = Puzzle(puzzlegrid)