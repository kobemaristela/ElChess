import pygame 
from pygame.locals import *

X, Y = 560, 560
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
board_colors = [blue, white]

# Define our square object and call super to
# give it all the properties and methods of pygame.sprite.Sprite
class Square(pygame.sprite.Sprite):
    def __init__(self, color):
        super(Square, self).__init__()
        self.color = color
        self.surf = pygame.Surface((70, 70))        # Define the dimension of the surface

        # define color of surface - black (0, 0, 0), white (255, 255, 255)
        self.surf.fill(self.color)
        self.rect = self.surf.get_rect()

class Pawn:
    def __init__(self):
        return


pygame.init()
square1 = Square(white)
#square2 = Square(blue)

# Define the dimensions of screen object
screen = pygame.display.set_mode((X, Y))
pygame.display.set_caption("ELCHESS")

title_font = pygame.font.SysFont("inkfree", 50)
font = pygame.font.SysFont("inkfree", 30)
welcome_text = title_font.render('Welcome to ELCHESS', True, white)
click_caption = font.render('-Click anywhere to start game-', True, (255, 0, 255)) #cyan
backspace_caption = font.render('-Backspace to QUIT game-', True, (0, 255, 255)) #magenta

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
            screen.fill(black)
            pygame.display.flip()
 
# Chessboard
while gameOn:

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_BACKSPACE:
                gameOn = False
        elif event.type == QUIT:
            gameOn = False

    square_coor = [(0, 0), (0, 140), (0, 280), (0, 420), (70, 70), (70, 210), (70, 350), (70, 490), 
                    (140, 0), (140, 140), (140, 280), (140, 420), (210, 70), (210, 210), (210, 350),
                    (210, 490), (280, 0), (280, 140), (280, 280), (280, 420), (350, 70), (350, 210),
                    (350, 350), (350, 490), (420, 0), (420, 140), (420, 280), (420, 420), (490, 70),
                    (490, 210), (490, 350), (490, 490)]
                        
    for coor in square_coor:
        screen.blit(square1.surf, coor)

    pygame.display.flip()