class Piece :
    def __init__(self, color,pos) :
        self.color = color
        self.pos = pos
    def move(self, new_pos) :
        self.pos = new_pos
    
class Pawn(Piece) :
    pass

class Rook(Piece) :
    pass

class Bishop(Piece) :
    pass

class Queen(Piece) :
    pass

class King(Piece) :
    pass

class Knight(Piece) :
    pass
    