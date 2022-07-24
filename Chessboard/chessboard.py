import pygame 
import sys
from pygame.locals import *
from board_constants import *

# Define our square object and call super to
# give it all the properties and methods of pygame.sprite.Sprite
class Square(pygame.sprite.Sprite):
    def __init__(self, color):
        super(Square, self).__init__()
        self.color = color
        self.surf = pygame.Surface((70, 70))

        self.surf.fill(self.color)
        self.rect = self.surf.get_rect()

class Pawn(pygame.sprite.Sprite):
    def __init__(self):
        super(Pawn, self).__init__()
        self.pawn_image = pygame.image.load("Pawn.png")
        self.pawn_image = pygame.transform.scale(self.pawn_image, (45, 55))

    def move(self):
        self.direction = "up"

    def attack(self, direction_str):
        self.direction = "up"
        self.direction = direction_str 

    def update(self):
        pos = pygame.mouse.get_pos()

def run():
    pawn1 = Pawn()
    pygame.init()

    screen = pygame.display.set_mode((X, Y))
    pygame.display.set_caption("ELCHESS")

    title_font = pygame.font.SysFont("inkfree", 50)
    font = pygame.font.SysFont("inkfree", 30)
    welcome_text = title_font.render('Welcome to ELCHESS', True, WHITE)
    click_caption = font.render('-Click anywhere to start game-', True, (255, 0, 255)) #cyan
    backspace_caption = font.render('-Backspace to QUIT game-', True, (0, 255, 255)) #magenta

    play = True

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
                    sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                play = False
                screen.fill(GRAY)
                pygame.display.flip()

    # Chessboard
    for color in board_colors:
        square1 = Square(color)
        gameOn = True
        while gameOn:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_BACKSPACE:
                        sys.exit()
                    elif event.key == K_SPACE:
                        gameOn = False
                    elif event.key == K_UP:
                        pawn1.move()
                    elif event.key == K_RIGHT:
                        pawn1.attack("right")
                    elif event.key == K_LEFT:
                        pawn1.attack("left")
                elif event.type == QUIT:
                    gameOn = False

            square_coor = [(0, 0), (0, 140), (0, 280), (0, 420), (70, 70), (70, 210), (70, 350), (70, 490), 
                (140, 0), (140, 140), (140, 280), (140, 420), (210, 70), (210, 210), (210, 350),
                (210, 490), (280, 0), (280, 140), (280, 280), (280, 420), (350, 70), (350, 210),
                (350, 350), (350, 490), (420, 0), (420, 140), (420, 280), (420, 420), (490, 70),
                (490, 210), (490, 350), (490, 490)]

            for coor in square_coor:
                screen.blit(square1.surf, coor)

            screen.blit(pawn1.pawn_image, (10, 80))
            pygame.display.flip()

if __name__ == "__main__":
    run()