import pygame, sys
from pygame.locals import *
from map_constants import *
from map_tiles import Map

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Elchess")
        self.clock = pygame.time.Clock()
        self.map = Map()

        #audio
        self.music = pygame.mixer.Sound('dungeon_music.wav')
        self.music.set_volume(0.5)
        self.music.play(-1)

    def homescreen(self):
        title_font = pygame.font.SysFont("inkfree", 70)
        font = pygame.font.SysFont("inkfree", 40)
        welcome_text = title_font.render('Welcome to ELCHESS', True, WHITE)
        click_caption = font.render('-Click anywhere to start game-', True, RED) #cyan
        backspace_caption = font.render('-Backspace to QUIT game-', True, GRAY) #magenta

        play = True
        while play:
            self.screen.blit(welcome_text, (110, 80))
            self.screen.blit(click_caption, (150, 300))
            self.screen.blit(backspace_caption, (180, 350))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_BACKSPACE:
                        play = False
                        sys.exit()
                elif event.type == MOUSEBUTTONDOWN:
                    play = False
                    self.screen.fill(BLACK)
                    pygame.display.flip()

    def run(self):
        # run and setup game here
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_BACKSPACE:
                        running = False

            self.screen.fill(BLACK)
            self.map.run()
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == "__main__":
    game = Game()
    game.homescreen()
    game.run()