from piece import * 
from player import *
class game:
    def __init__(self, board, wplayer1, bplayer2):
        self.board = board
        self.wplayer1 = wplayer1
        self.bplayer2 = bplayer2

    def start(self): #to start the game by placing the pieces in their initial positions
        wrook1 = Rook("white",(0,0))
        wknight1 = Knight("white",(1,0))
        wbishop1 = Bishop("white",(2,0))
        wqueen = Queen("white",(3,0))
        wking = King("white",(4,0))
        wbishop2 = Bishop("white",(5,0))
        wknight2 = Knight("white",(6,0))
        wrook2 = Rook("white",(7,0))
        wpawn1 = Pawn("white",(0,1))
        wpawn2 = Pawn("white",(1,1))
        wpawn3 = Pawn("white",(2,1))
        wpawn4 = Pawn("white",(3,1))
        wpawn5 = Pawn("white",(4,1))
        wpawn6 = Pawn("white",(5,1))
        wpawn7 = Pawn("white",(6,1))
        wpawn8 = Pawn("white",(7,1))

        brook1 = Rook("black",(0,7))
        bknight1 = Knight("black",(1,7))
        bbishop1 = Bishop("black",(2,7))
        bqueen = Queen("black",(3,7))
        bking = King("black",(4,7))
        bbishop2 = Bishop("black",(5,7))
        bknight2 = Knight("black",(6,7))
        brook2 = Rook("black",(7,7))
        bpawn1 = Pawn("black",(0,6))
        bpawn2 = Pawn("black",(1,6))
        bpawn3 = Pawn("black",(2,6))
        bpawn4 = Pawn("black",(3,6))
        bpawn5 = Pawn("black",(4,6))
        bpawn6 = Pawn("black",(5,6))
        bpawn7 = Pawn("black",(6,6))
        bpawn8 = Pawn("black",(7,6))


        self.board.board[0][0] = wrook1
        self.board.board[1][0] = wknight1
        self.board.board[2][0] = wbishop1
        self.board.board[3][0] = wqueen
        self.board.board[4][0] = wking
        self.board.board[5][0] = wbishop2
        self.board.board[6][0] = wknight2
        self.board.board[7][0] = wrook2
        self.board.board[0][1] = wpawn1
        self.board.board[1][1] = wpawn2
        self.board.board[2][1] = wpawn3
        self.board.board[3][1] = wpawn4
        self.board.board[4][1] = wpawn5
        self.board.board[5][1] = wpawn6
        self.board.board[6][1] = wpawn7
        self.board.board[7][1] = wpawn8

        self.board.board[0][7] = brook1
        self.board.board[1][7] = bknight1
        self.board.board[2][7] = bbishop1
        self.board.board[3][7] = bqueen
        self.board.board[4][7] = bking
        self.board.board[5][7] = bbishop2
        self.board.board[6][7] = bknight2
        self.board.board[7][7] = brook2
        self.board.board[0][6] = bpawn1
        self.board.board[1][6] = bpawn2
        self.board.board[2][6] = bpawn3
        self.board.board[3][6] = bpawn4
        self.board.board[4][6] = bpawn5
        self.board.board[5][6] = bpawn6
        self.board.board[6][6] = bpawn7
        self.board.board[7][6] = bpawn8

        self.wplayer1.pieces = [wking,wrook1,wknight1,wbishop1,wqueen,wbishop2,wknight2,wrook2,wpawn1,wpawn2,wpawn3,wpawn4,wpawn5,wpawn6,wpawn7,wpawn8]
        self.bplayer2.pieces = [bking,brook1,bknight1,bbishop1,bqueen,bbishop2,bknight2,brook2,bpawn1,bpawn2,bpawn3,bpawn4,bpawn5,bpawn6,bpawn7,bpawn8]

    def eat_piece(self, piece): #to remove a piece from the board and from the player's pieces when it's eaten by the opponent
        if piece.color == "white":
            self.wplayer1.sup_piece(piece)
        else:
            self.bplayer2.sup_piece(piece)
    
    def checkmate(self, player): #to check if the player is in checkmate
        if player.color == "white":
            opponent_pieces = self.bplayer2.pieces
            king_pos = self.wplayer1.pieces[0].pos
        else:
            opponent_pieces = self.wplayer1.pieces
            king_pos = self.bplayer2.pieces[0].pos
        
        for piece in opponent_pieces:
            if piece.can_move(king_pos):
                return True
        return False
    
    def stalemate(self, player): #to check if the player is in stalemate
        if player.color == "white":
            opponent_pieces = self.bplayer2.pieces
            king_pos = self.wplayer1.pieces[0].pos
        else:
            opponent_pieces = self.wplayer1.pieces
            king_pos = self.bplayer2.pieces[0].pos
        
        for piece in opponent_pieces:
            if piece.can_move(king_pos):
                return False
        return True
    
    def draw(self): #to check if the game is a draw
        if len(self.wplayer1.pieces) == 1 and len(self.bplayer2.pieces) == 1:
            return True
        return False
    
    def resign(self, player,resign=False): #to allow the player to resign
        if player.color == "white" and resign==True:
            return "black wins"
        elif player.color == "black" and resign==True:
            return "white wins" 
    
    def end_game(self, player,resign=False): #to end the game when a player is in checkmate, stalemate, draw or resigns
        if self.checkmate(player):
            if player.color == "white":
                return "black wins"
            else:
                return "white wins"
        elif self.stalemate(player):
            return "stalemate"
        elif self.draw():
            return "draw"
        elif resign==True:
            return self.resign(player,resign)
        
    def end_turn(self, player, endturn=False): #to end the turn for the player and start the timer for the opponent
        if player.color == "white" and endturn==True:
            self.bplayer2.timer(self.bplayer2.time)
        elif player.color == "black" and endturn==True:
            self.wplayer1.timer(self.wplayer1.time)
    
    def play_turn(self, player, piece, new_pos):
        if piece.color != player.color:
            return "invalid move"
        old_pos = piece.pos
        if self.board.Taken_box(new_pos):
            self.eat_piece(self.board.ReturnPiece(new_pos))
        piece.move(new_pos)
        self.board.board[new_pos[0]][new_pos[1]] = piece
        self.board.board[old_pos[0]][old_pos[1]] = 0
        self.end_turn(player, endturn=True)
        return self.end_game(player)