import pygame 
from pygame.locals import *

X, Y = 560, 560

class Square(pygame.sprite.Sprite):
    
    def __init__(self):
        super(Square, self).__init__()

        # Define the dimension of the surface
        self.surf = pygame.Surface((70, 70))

        # define color of surface - black (0, 0, 0), white (255, 255, 255)
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()

pygame.init()

# Define the dimensions of screen object
screen = pygame.display.set_mode((X, Y))
pygame.display.set_caption("ELCHESS")

title_font = pygame.font.SysFont("inkfree", 50)
font = pygame.font.SysFont("inkfree", 30)
welcome_text = title_font.render('Welcome to ELCHESS', True, (255, 255, 255))
click_caption = font.render('-Click anywhere to start game-', True, (255, 0, 255))
backspace_caption = font.render('-Backspace to QUIT game-', True, (0, 255, 255))

square1 = Square()

play = True
gameOn = True

# Homescreen
while play:
    screen.blit(welcome_text, (70, 120))
    screen.blit(click_caption, (80, 300))
    screen.blit(backspace_caption, (100, 350))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_BACKSPACE:
                play = False
                gameOn = False
        elif event.type == MOUSEBUTTONDOWN:
            play = False
            screen.fill((0, 0, 0))
            pygame.display.flip()
 
# Chessboard
while gameOn:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_BACKSPACE:
                gameOn = False
                 
        # Check for QUIT event
        elif event.type == QUIT:
            gameOn = False
 
    # first column
    screen.blit(square1.surf, (0, 0))
    screen.blit(square1.surf, (0, 140))
    screen.blit(square1.surf, (0, 280))
    screen.blit(square1.surf, (0, 420))

    # Second column
    screen.blit(square1.surf, (70, 70))
    screen.blit(square1.surf, (70, 210))
    screen.blit(square1.surf, (70, 350))
    screen.blit(square1.surf, (70, 490))

    # Third column
    screen.blit(square1.surf, (140, 0))
    screen.blit(square1.surf, (140, 140))
    screen.blit(square1.surf, (140, 280))
    screen.blit(square1.surf, (140, 420))
    
    # fourth column
    screen.blit(square1.surf, (210, 70))
    screen.blit(square1.surf, (210, 210))
    screen.blit(square1.surf, (210, 350))
    screen.blit(square1.surf, (210, 490))

    # Fifth column
    screen.blit(square1.surf, (280, 0))
    screen.blit(square1.surf, (280, 140))
    screen.blit(square1.surf, (280, 280))
    screen.blit(square1.surf, (280, 420))

    # Sixth column
    screen.blit(square1.surf, (350, 70))
    screen.blit(square1.surf, (350, 210))
    screen.blit(square1.surf, (350, 350))
    screen.blit(square1.surf, (350, 490))

    # Seventh column
    screen.blit(square1.surf, (420, 0))
    screen.blit(square1.surf, (420, 140))
    screen.blit(square1.surf, (420, 280))
    screen.blit(square1.surf, (420, 420))

    # Eigth column
    screen.blit(square1.surf, (490, 70))
    screen.blit(square1.surf, (490, 210))
    screen.blit(square1.surf, (490, 350))
    screen.blit(square1.surf, (490, 490))
 
    pygame.display.flip()