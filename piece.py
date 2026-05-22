class Piece :
    def __init__(self, color,pos) :
        self.color = color
        self.pos = pos
    def move(self, new_pos) :
        self.pos = new_pos
    def can_move(self, new_pos) :
        return False
    
class Pawn(Piece) :
    def move(self, new_pos) : #to move the pawn one or two steps forward if it's the first move, and one step forward otherwise
        if self.color == "white" :
            if ( self.pos[1]==1) :
               if (new_pos[1] == self.pos[1] + 1 and new_pos[0] == self.pos[0] or (new_pos[1] == self.pos[1] + 2 and new_pos[0] == self.pos[0])) :
                    self.pos = new_pos
            else :
                if (new_pos[1] == self.pos[1] + 1 and new_pos[0] == self.pos[0]) :
                    self.pos = new_pos
        else :
            if ( self.pos[1]==6) :
               if (new_pos[1] == self.pos[1] - 1 and new_pos[0] == self.pos[0] or (new_pos[1] == self.pos[1] - 2 and new_pos[0] == self.pos[0])) :
                    self.pos = new_pos
            else :
                if (new_pos[1] == self.pos[1] - 1 and new_pos[0] == self.pos[0]) :
                    self.pos = new_pos
    def can_move(self, new_pos) :
        if self.color == "white" :
            if ( self.pos[1]==1) :
               if (new_pos[1] == self.pos[1] + 1 and new_pos[0] == self.pos[0] or (new_pos[1] == self.pos[1] + 2 and new_pos[0] == self.pos[0])) :
                    return True
            else :
                if (new_pos[1] == self.pos[1] + 1 and new_pos[0] == self.pos[0]) :
                    return True
        else :
            if ( self.pos[1]==6) :
               if (new_pos[1] == self.pos[1] - 1 and new_pos[0] == self.pos[0] or (new_pos[1] == self.pos[1] - 2 and new_pos[0] == self.pos[0])) :
                    return True
            else :
                if (new_pos[1] == self.pos[1] - 1 and new_pos[0] == self.pos[0]) :
                    return True
        return False
class Rook(Piece) : #to move the rook in a straight line either horizontally or vertically
    def move(self, new_pos) :
        if (new_pos[0] == self.pos[0] or new_pos[1] == self.pos[1]) :
            self.pos = new_pos

    def can_move(self, new_pos) :
        if (new_pos[0] == self.pos[0] or new_pos[1] == self.pos[1]) :
            return True
        return False

class Bishop(Piece) : #to move the bishop in a straight line diagonally
    def move(self, new_pos) :
        for i in range(-7,8) :
            if ((new_pos[0] == self.pos[0]+i and new_pos[1] == self.pos[1]+i )or (new_pos[0] == self.pos[0]+i and new_pos[1] == self.pos[1]-i)) :
                self.pos = new_pos

    def can_move(self, new_pos) :
        for i in range(-7,8) :
            if ((new_pos[0] == self.pos[0]+i and new_pos[1] == self.pos[1]+i )or (new_pos[0] == self.pos[0]+i and new_pos[1] == self.pos[1]-i)) :
                return True
        return False

class Queen(Piece) : #to move the queen in a straight line either horizontally, vertically or diagonally
    def can_move(self, new_pos) :
        if new_pos[0] == self.pos[0] or new_pos[1] == self.pos[1] :
            return True
        else :
            for i in range(-7,8) :
                if ((new_pos[0] == self.pos[0]+i and new_pos[1] == self.pos[1]+i )or (new_pos[0] == self.pos[0]+i and new_pos[1] == self.pos[1]-i)) :
                    return True
        return False
    
    def move(self, new_pos) :
        if new_pos[0] == self.pos[0] or new_pos[1] == self.pos[1] :
            self.pos = new_pos
        else :
            for i in range(-7,8) :
                if ((new_pos[0] == self.pos[0]+i and new_pos[1] == self.pos[1]+i )or (new_pos[0] == self.pos[0]+i and new_pos[1] == self.pos[1]-i)) :
                    self.pos = new_pos

class King(Piece) : #to move the king one step in any direction
    def move(self, new_pos) :
        for i in range(-1,2) :
            for j in range(-1,2) :
                if (new_pos[0] == self.pos[0]+i and new_pos[1] == self.pos[1] +j):
                    self.pos = new_pos
    
    def can_move(self, new_pos) :
        for i in range(-1,2) :
            for j in range(-1,2) :
                if (new_pos[0] == self.pos[0]+i and new_pos[1] == self.pos[1] +j):
                    return True
        return False

class Knight(Piece) : #to move the knight in an L shape
    def move(self, new_pos) :
        if ((new_pos[0] == self.pos[0]+1 and new_pos[1] == self.pos[1]+2) or (new_pos[0] == self.pos[0]+1 and new_pos[1] == self.pos[1]-2) or (new_pos[0] == self.pos[0]+2 and new_pos[1] == self.pos[1]+1) or (new_pos[0] == self.pos[0]+2 and new_pos[1] == self.pos[1]-1) or(new_pos[0]==self.pos[0]-2 and new_pos[1] == self.pos[1]+1) or (new_pos[0] == self.pos[0]-2 and new_pos[1] == self.pos[1]-1) or (new_pos[0] == self.pos[0]-1 and new_pos[1] == self.pos[1]+2) or (new_pos[0] == self.pos[0]-1 and new_pos[1] == self.pos[1]-2) ):
            self.pos = new_pos
    
    def can_move(self, new_pos) :
        if ((new_pos[0] == self.pos[0]+1 and new_pos[1] == self.pos[1]+2) or (new_pos[0] == self.pos[0]+1 and new_pos[1] == self.pos[1]-2) or (new_pos[0] == self.pos[0]+2 and new_pos[1] == self.pos[1]+1) or (new_pos[0] == self.pos[0]+2 and new_pos[1] == self.pos[1]-1) or(new_pos[0]==self.pos[0]-2 and new_pos[1] == self.pos[1]+1) or (new_pos[0] == self.pos[0]-2 and new_pos[1] == self.pos[1]-1) or (new_pos[0] == self.pos[0]-1 and new_pos[1] == self.pos[1]+2) or (new_pos[0] == self.pos[0]-1 and new_pos[1] == self.pos[1]-2) ):
            return True
        return False