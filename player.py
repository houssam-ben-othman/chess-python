import time 
class Player:
    def __init__(self, name, color, s):
        self.name = name
        self.color = color
        self.pieces = []
        self.time = s

    def timer(self,s): #to create a timer for each player
        def wrapper(s, t):
            while True:
                yield time.time() - t <= s
        return wrapper(s, time.time())
    
    def end_timer(self,time): #to end the timer for the player
        self.endtime = self.timer(time)

    def sup_piece(self, piece): #to remove a piece from the player's pieces when it's eaten by the opponent
        self.pieces.remove(piece)
 
 
