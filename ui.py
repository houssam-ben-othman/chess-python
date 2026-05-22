import pygame
import time

pygame.init()
taille_fenetre = (800, 800) 
screen = pygame.display.set_mode(taille_fenetre)
pygame.display.set_caption("Chess Game")



def draw_board():
    colors = [(220, 200, 170), (45, 30, 20)] 
    for row in range(8):
        for col in range(8):
            color = colors[(row + col) % 2] 
            pygame.draw.rect(screen, color, (col * 100, row * 100, 100, 100))








continuer = True
while continuer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
    draw_board()
    pygame.display.flip()

pygame.quit()