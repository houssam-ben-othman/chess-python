import time 
class Player:
    def __init__(self, color,s):
        self.color = color
        self.score = 0
        self.pieces = []
        self.time=s

    def timer(self,s):
        def wrapper(s, t):
            while True:
                yield time.time() - t <= s
        return wrapper(s, time.time())
    
    def end_timer(self,time):
        self.endtime = self.timer(time)

    def sup_piece(self, piece):
        self.pieces.remove(piece)
 
 
