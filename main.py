from game import *
from board import *
from player import *
from piece import *

if __name__ == "__main__":
    print("Welcome to Chess!")
    print("Player 1 is white and Player 2 is black.")
    print("To move a piece, enter the coordinates of the piece you want to move and the coordinates of the destination.")
    print("For example, to move a piece from e2 to e4, enter 'e2 e4'.")
    print("To resign, enter 'resign'.")
    print("Let's start the game!")
    print("Player 1 (white), please enter your name:")
    player1_name = input()
    print("Player 2 (black), please enter your name:")
    player2_name = input()
    white_player = Player(player1_name,"white", 600)
    black_player = Player(player2_name,"black", 600)
    b = Board()
    chess_game = game(b,white_player, black_player)
    chess_game.start()
    while chess_game.endgame==False:
        if chess_game.turn == "white":
            print("Player 1 (white), it's your turn.")
            move = input()
            if move == "resign":
                print(chess_game.end_game(white_player,resign=True))
                break
            else:
                move = move.split()
                start_pos = b.cord_to_pos(move[0])
                end_pos = b.cord_to_pos(move[1])
                result = chess_game.move_piece(white_player, start_pos, end_pos)
                if result:
                    print("Move successful!")
                else:
                    print("Invalid move. Please try again.")
        else:
            print("Player 2 (black), it's your turn.")
            move = input()
            if move == "resign":
                print(chess_game.end_game(black_player,resign=True))
                break
            else:
                move = move.split()
                start_pos = b.cord_to_pos(move[0])
                end_pos = b.cord_to_pos(move[1])
                result = chess_game.move_piece(black_player, start_pos, end_pos)
                if result:
                    print("Move successful!")
                else:
                    print("Invalid move. Please try again.")
            