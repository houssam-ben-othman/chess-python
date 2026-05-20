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
    
    def cord_to_pos(self, cord): #to convert the coordinates to the position in the board
        x = ord(cord[0]) - ord('a')
        y = int(cord[1]) - 1
        return (x,y)