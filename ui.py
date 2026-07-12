import pygame
import time
from game import *
from board import *
from player import *
from piece import *

pygame.init()
taille_fenetre = (800, 900)
screen = pygame.display.set_mode(taille_fenetre)
pygame.display.set_caption("Chess Game")

font_pieces = pygame.font.SysFont("segoeuisymbol", 70)
font_info = pygame.font.SysFont("Arial", 24)

piece_symboles = {
    "Pawn":   {"white": "♙", "black": "♟"},
    "Rook":   {"white": "♖", "black": "♜"},
    "Knight": {"white": "♘", "black": "♞"},
    "Bishop": {"white": "♗", "black": "♝"},
    "Queen":  {"white": "♕", "black": "♛"},
    "King":   {"white": "♔", "black": "♚"},
}

def board_to_screen(pos): #to convert board position (col, row) to pygame pixel position
    pygame_x = pos[0] * 100
    pygame_y = (7 - pos[1]) * 100
    return (pygame_x, pygame_y)

def screen_to_board(pixel_x, pixel_y): #to convert pygame pixel position to board position (col, row)
    col = pixel_x // 100
    row = 7 - (pixel_y // 100)
    return (col, row)

def draw_board():
    colors = [(220, 200, 170), (45, 30, 20)]
    for row in range(8):
        for col in range(8):
            color = colors[(row + col) % 2]
            pygame.draw.rect(screen, color, (col * 100, row * 100, 100, 100))

def draw_highlight(pos, color):
    pygame_x, pygame_y = board_to_screen(pos)
    pygame.draw.rect(screen, color, (pygame_x, pygame_y, 100, 100), 5)

def draw_pieces(board):
    for col in range(8):
        for row in range(8):
            piece = board.board[col][row]
            if piece != 0 :
                piece_type = type(piece).__name__
                symbole = piece_symboles[piece_type][piece.color]
                if piece.color == "white":
                    couleur_texte = (255, 255, 255)
                else:
                    couleur_texte = (10, 10, 10)
                texte = font_pieces.render(symbole, True, couleur_texte)
                pygame_x, pygame_y = board_to_screen((col, row))
                screen.blit(texte, (pygame_x + 15, pygame_y + 10))

def draw_info(message, tour):
    pygame.draw.rect(screen, (30, 30, 30), (0, 800, 800, 100))
    if tour == "white":
        couleur_tour = (255, 255, 255)
        texte_tour = font_info.render("Tour : Blanc", True, couleur_tour)
    else:
        couleur_tour = (180, 180, 180)
        texte_tour = font_info.render("Tour : Noir", True, couleur_tour)
    screen.blit(texte_tour, (20, 815))
    if message != "":
        texte_msg = font_info.render(message, True, (255, 220, 50))
        screen.blit(texte_msg, (20, 850))

def setup_players():
    white_player = Player("Joueur 1", "white", 600)
    black_player = Player("Joueur 2", "black", 600)
    return white_player, black_player

white_player, black_player = setup_players()
b = Board()
chess_game = game(b, white_player, black_player)
chess_game.start()

selected_pos = None
message = ""
continuer = True

while continuer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False

        if event.type == pygame.MOUSEBUTTONDOWN and chess_game.endgame == False:
            pixel_x, pixel_y = event.pos
            if pixel_y < 800:
                clicked_pos = screen_to_board(pixel_x, pixel_y)

                if selected_pos is None:
                    piece = b.ReturnPiece(clicked_pos)
                    if piece != 0 and piece.color == chess_game.turn:
                        selected_pos = clicked_pos
                        message = ""
                else:
                    if chess_game.turn == "white":
                        current_player = white_player
                    else:
                        current_player = black_player

                    result = chess_game.move_piece(current_player, selected_pos, clicked_pos)
                    if result == True:
                        message = "Coup valide !"
                    elif result == False:
                        message = "Coup invalide, reessayez."
                    elif result == "black wins":
                        message = "Les noirs gagnent ! Partie terminee."
                        chess_game.endgame = True
                    elif result == "white wins":
                        message = "Les blancs gagnent ! Partie terminee."
                        chess_game.endgame = True
                    elif result == "draw":
                        message = "Match nul !"
                        chess_game.endgame = True
                    selected_pos = None

    screen.fill((0, 0, 0))
    draw_board()

    if selected_pos is not None:
        draw_highlight(selected_pos, (50, 200, 50))

    draw_pieces(b)
    draw_info(message, chess_game.turn)
    pygame.display.flip()

pygame.quit()