class Piece :
    def __init__(self, color,pos) :
        self.color = color
        self.pos = pos
    def move(self, new_pos) :
        self.pos = new_pos
    
class Pawn(Piece) :
    def move(self, new_pos) :
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

class Rook(Piece) :
    def move(self, new_pos) :
        if (new_pos[0] == self.pos[0] or new_pos[1] == self.pos[1]) :
            self.pos = new_pos

class Bishop(Piece) :
    def move(self, new_pos) :
        for i in range(-7,8) :
            if ((new_pos[0] == self.pos[0]+i and new_pos[1] == self.pos[1]+i )or (new_pos[0] == self.pos[0]+i and new_pos[1] == self.pos[1]-i)) :
                self.pos = new_pos
                break

class Queen(Piece) :
    def move(self, new_pos) :
        if new_pos[0] == self.pos[0] or new_pos[1] == self.pos[1] :
            self.pos = new_pos
        else :
            for i in range(-7,8) :
                if ((new_pos[0] == self.pos[0]+i and new_pos[1] == self.pos[1]+i )or (new_pos[0] == self.pos[0]+i and new_pos[1] == self.pos[1]-i)) :
                    self.pos = new_pos
                    break

class King(Piece) :
    def move(self, new_pos) :
        flag=False
        for i in range(-1,2) :
            for j in range(-1,2) :
                if (new_pos[0] == self.pos[0]+i and new_pos[1] == self.pos[1] +j):
                    self.pos = new_pos
                    flag=True
                    break
            if (flag==True):
                    break

class Knight(Piece) :
    def move(self, new_pos) :
        if ((new_pos[0] == self.pos[0]+1 and new_pos[1] == self.pos[1]+2) or (new_pos[0] == self.pos[0]+1 and new_pos[1] == self.pos[1]-2) or (new_pos[0] == self.pos[0]+2 and new_pos[1] == self.pos[1]+1) or (new_pos[0] == self.pos[0]+2 and new_pos[1] == self.pos[1]-1) or(new_pos[0]==self.pos[0]-2 and new_pos[1] == self.pos[1]+1) or (new_pos[0] == self.pos[0]-2 and new_pos[1] == self.pos[1]-1) or (new_pos[0] == self.pos[0]-1 and new_pos[1] == self.pos[1]+2) or (new_pos[0] == self.pos[0]-1 and new_pos[1] == self.pos[1]-2) ):
            self.pos = new_pos
    