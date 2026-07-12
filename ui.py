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

def format_timer(secondes) :
    minutes = int(secondes) // 60
    secs = int(secondes) % 60
    return f"{minutes:02}:{secs:02}"

def draw_info(message, tour, temps_blanc, temps_noir) :
    pygame.draw.rect(screen, (30, 30, 30), (0, 800, 800, 100))
    if tour == "white" :
        couleur_tour = (255, 255, 255)
        texte_tour = font_info.render("Tour : Blanc", True, couleur_tour)
    else :
        couleur_tour = (180, 180, 180)
        texte_tour = font_info.render("Tour : Noir", True, couleur_tour)
    screen.blit(texte_tour, (20, 810))
    if temps_blanc <= 30 :
        couleur_blanc = (255, 80, 80)
    else :
        couleur_blanc = (255, 255, 255)
    if temps_noir <= 30 :
        couleur_noir = (255, 80, 80)
    else :
        couleur_noir = (180, 180, 180)
    texte_blanc = font_info.render("Blanc : " + format_timer(temps_blanc), True, couleur_blanc)
    texte_noir = font_info.render("Noir : " + format_timer(temps_noir), True, couleur_noir)
    screen.blit(texte_blanc, (20, 840))
    screen.blit(texte_noir, (250, 840))
    if message != "" :
        texte_msg = font_info.render(message, True, (255, 220, 50))
        screen.blit(texte_msg, (500, 840))

def setup_players():
    white_player = Player("Joueur 1", "white", 600)
    black_player = Player("Joueur 2", "black", 600)
    return white_player, black_player






# Main loop of the game
white_player, black_player = setup_players()
b = Board()
chess_game = game(b, white_player, black_player)
chess_game.start()

selected_pos = None
message = ""
temps_blanc = 600.0
temps_noir = 600.0
temps_debut_tour = time.time()
continuer = True

while continuer :
    temps_ecoule = time.time() - temps_debut_tour

    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            continuer = False

        if event.type == pygame.MOUSEBUTTONDOWN and chess_game.endgame == False :
            pixel_x, pixel_y = event.pos
            if pixel_y < 800 :
                clicked_pos = screen_to_board(pixel_x, pixel_y)

                if selected_pos is None :
                    piece = b.ReturnPiece(clicked_pos)
                    if piece != 0 and piece.color == chess_game.turn :
                        selected_pos = clicked_pos
                        message = ""
                else :
                    if chess_game.turn == "white" :
                        current_player = white_player
                    else :
                        current_player = black_player

                    result = chess_game.move_piece(current_player, selected_pos, clicked_pos)
                    if result == True :
                        message = "Coup valide !"
                        if current_player.color == "white" :
                            temps_blanc -= temps_ecoule
                        else :
                            temps_noir -= temps_ecoule
                        temps_debut_tour = time.time()
                    elif result == False :
                        message = "Coup invalide, reessayez."
                    elif result == "black wins" :
                        message = "Les noirs gagnent !"
                        chess_game.endgame = True
                    elif result == "white wins" :
                        message = "Les blancs gagnent !"
                        chess_game.endgame = True
                    elif result == "draw" :
                        message = "Match nul !"
                        chess_game.endgame = True
                    selected_pos = None

    if chess_game.endgame == False :
        if chess_game.turn == "white" :
            temps_blanc_affiche = max(0, temps_blanc - temps_ecoule)
            temps_noir_affiche = max(0, temps_noir)
        else :
            temps_blanc_affiche = max(0, temps_blanc)
            temps_noir_affiche = max(0, temps_noir - temps_ecoule)
        if temps_blanc_affiche == 0 :
            message = "Temps ecoule ! Les noirs gagnent."
            chess_game.endgame = True
        if temps_noir_affiche == 0 :
            message = "Temps ecoule ! Les blancs gagnent."
            chess_game.endgame = True
    else :
        temps_blanc_affiche = max(0, temps_blanc)
        temps_noir_affiche = max(0, temps_noir)

    screen.fill((0, 0, 0))
    draw_board()

    if selected_pos is not None :
        draw_highlight(selected_pos, (50, 200, 50))

    draw_pieces(b)
    draw_info(message, chess_game.turn, temps_blanc_affiche, temps_noir_affiche)
    pygame.display.flip()

pygame.quit()
