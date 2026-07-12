class Piece :
    def __init__(self, color, pos) :
        self.color = color
        self.pos = pos
    def move(self, new_pos) :
        self.pos = new_pos
    def can_move(self, new_pos) :
        return False

class Pawn(Piece) :
    def move_piece(self, player, start_pos, end_pos):
        piece = self.board.ReturnPiece(start_pos)
        if piece == 0:
            return False
        if piece.color != player.color:
            return False
        if self.board.Taken_box(end_pos) and self.board.ReturnPiece(end_pos).color == player.color:
            return False
        if type(piece).__name__ == "Pawn":
            if end_pos[0] == start_pos[0]:
                if not piece.can_move(end_pos):
                    return False
                if self.board.Taken_box(end_pos):
                    return False
            else:
                if not self.board.Taken_box(end_pos):
                    return False
                if piece.color == "white":
                    if not (end_pos[1] == start_pos[1] + 1 and (end_pos[0] == start_pos[0] + 1 or end_pos[0] == start_pos[0] - 1)):
                        return False
                else:
                    if not (end_pos[1] == start_pos[1] - 1 and (end_pos[0] == start_pos[0] + 1 or end_pos[0] == start_pos[0] - 1)):
                        return False
        else:
            if not piece.can_move(end_pos):
                return False
        resultat = self.play_turn(player, piece, end_pos)
        if resultat is not None:
            return resultat
        return True

    def can_move(self, new_pos) :
        if self.color == "white" :
            if (self.pos[1] == 1) :
                if (new_pos[1] == self.pos[1] + 1 and new_pos[0] == self.pos[0] or (new_pos[1] == self.pos[1] + 2 and new_pos[0] == self.pos[0])) :
                    return True
            else :
                if (new_pos[1] == self.pos[1] + 1 and new_pos[0] == self.pos[0]) :
                    return True
            if (new_pos[1] == self.pos[1] + 1 and (new_pos[0] == self.pos[0] + 1 or new_pos[0] == self.pos[0] - 1)) :
                return True
        else :
            if (self.pos[1] == 6) :
                if (new_pos[1] == self.pos[1] - 1 and new_pos[0] == self.pos[0] or (new_pos[1] == self.pos[1] - 2 and new_pos[0] == self.pos[0])) :
                    return True
            else :
                if (new_pos[1] == self.pos[1] - 1 and new_pos[0] == self.pos[0]) :
                    return True
            if (new_pos[1] == self.pos[1] - 1 and (new_pos[0] == self.pos[0] + 1 or new_pos[0] == self.pos[0] - 1)) :
                return True
        return False

class Rook(Piece) :
    def move(self, new_pos) :
        if ((new_pos[0] == self.pos[0] or new_pos[1] == self.pos[1]) and new_pos != self.pos) :
            self.pos = new_pos
    def can_move(self, new_pos) :
        if ((new_pos[0] == self.pos[0] or new_pos[1] == self.pos[1]) and new_pos != self.pos) :
            return True
        return False

class Bishop(Piece) :
    def move(self, new_pos) :
        for i in range(-7, 8) :
            if i != 0 :
                if ((new_pos[0] == self.pos[0]+i and new_pos[1] == self.pos[1]+i) or (new_pos[0] == self.pos[0]+i and new_pos[1] == self.pos[1]-i)) :
                    self.pos = new_pos
    def can_move(self, new_pos) :
        for i in range(-7, 8) :
            if i != 0 :
                if ((new_pos[0] == self.pos[0]+i and new_pos[1] == self.pos[1]+i) or (new_pos[0] == self.pos[0]+i and new_pos[1] == self.pos[1]-i)) :
                    return True
        return False

class Queen(Piece) :
    def can_move(self, new_pos) :
        if (new_pos[0] == self.pos[0] or new_pos[1] == self.pos[1]) and new_pos != self.pos :
            return True
        else :
            for i in range(-7, 8) :
                if i != 0 :
                    if ((new_pos[0] == self.pos[0]+i and new_pos[1] == self.pos[1]+i) or (new_pos[0] == self.pos[0]+i and new_pos[1] == self.pos[1]-i)) :
                        return True
        return False
    def move(self, new_pos) :
        if (new_pos[0] == self.pos[0] or new_pos[1] == self.pos[1]) and new_pos != self.pos :
            self.pos = new_pos
        else :
            for i in range(-7, 8) :
                if i != 0 :
                    if ((new_pos[0] == self.pos[0]+i and new_pos[1] == self.pos[1]+i) or (new_pos[0] == self.pos[0]+i and new_pos[1] == self.pos[1]-i)) :
                        self.pos = new_pos

class King(Piece) :
    def move(self, new_pos) :
        for i in range(-1, 2) :
            for j in range(-1, 2) :
                if not (i == 0 and j == 0) :
                    if (new_pos[0] == self.pos[0]+i and new_pos[1] == self.pos[1]+j) :
                        self.pos = new_pos
    def can_move(self, new_pos) :
        for i in range(-1, 2) :
            for j in range(-1, 2) :
                if not (i == 0 and j == 0) :
                    if (new_pos[0] == self.pos[0]+i and new_pos[1] == self.pos[1]+j) :
                        return True
        return False

class Knight(Piece) :
    def move(self, new_pos) :
        if ((new_pos[0] == self.pos[0]+1 and new_pos[1] == self.pos[1]+2) or
            (new_pos[0] == self.pos[0]+1 and new_pos[1] == self.pos[1]-2) or
            (new_pos[0] == self.pos[0]+2 and new_pos[1] == self.pos[1]+1) or
            (new_pos[0] == self.pos[0]+2 and new_pos[1] == self.pos[1]-1) or
            (new_pos[0] == self.pos[0]-2 and new_pos[1] == self.pos[1]+1) or
            (new_pos[0] == self.pos[0]-2 and new_pos[1] == self.pos[1]-1) or
            (new_pos[0] == self.pos[0]-1 and new_pos[1] == self.pos[1]+2) or
            (new_pos[0] == self.pos[0]-1 and new_pos[1] == self.pos[1]-2)) :
            self.pos = new_pos
    def can_move(self, new_pos) :
        if ((new_pos[0] == self.pos[0]+1 and new_pos[1] == self.pos[1]+2) or
            (new_pos[0] == self.pos[0]+1 and new_pos[1] == self.pos[1]-2) or
            (new_pos[0] == self.pos[0]+2 and new_pos[1] == self.pos[1]+1) or
            (new_pos[0] == self.pos[0]+2 and new_pos[1] == self.pos[1]-1) or
            (new_pos[0] == self.pos[0]-2 and new_pos[1] == self.pos[1]+1) or
            (new_pos[0] == self.pos[0]-2 and new_pos[1] == self.pos[1]-1) or
            (new_pos[0] == self.pos[0]-1 and new_pos[1] == self.pos[1]+2) or
            (new_pos[0] == self.pos[0]-1 and new_pos[1] == self.pos[1]-2)) :
            return True
        return False