class Board:
    def __init__(self):
        self.board = [[0 for _ in range(8)] for _ in range(8)]

    def Taken_box(self, pos): #to check if the box is taken or not
        if self.board[pos[0]][pos[1]] != 0:
            return True
        else:
            return False
    
    def ReturnPiece(self, pos): #to return the piece in the given position
        return self.board[pos[0]][pos[1]]