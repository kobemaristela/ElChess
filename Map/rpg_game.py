import pygame, sys
import pathlib
from pygame.locals import *
from map_constants import *
from map_tiles import Map
from map_tiles import Button


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Elchess")
        self.clock = pygame.time.Clock()
        self.map = Map()

        #audio
        self.music = pygame.mixer.Sound(pathlib.Path(__file__).parent.parent /  'Graphics-Audio/dungeon_music.wav')
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
        attack_button_img = pygame.image.load(pathlib.Path(__file__).parent.parent  / 'Graphics-Audio/attack_button.png').convert_alpha()
        flee_button_img = pygame.image.load(pathlib.Path(__file__).parent.parent  / 'Graphics-Audio/flee_button.png').convert_alpha()
        player_attack_button = Button(50, 450, attack_button_img, 0.65)
        player_flee_button = Button(450, 450, flee_button_img, 0.65)


        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_BACKSPACE:
                        running = False

            # monster_to_attack = pygame.sprite.spritecollideany(hero, monsters)
            # if monster_to_attack:
            #     if player_attack_button.draw(screen):
            #         print(monster_to_attack)
            #         hero.attack(monster_to_attack)
            #         print(monster_to_attack)

            #         if monster_to_attack.hp <= 0:
            #             monster_to_attack.kill()
                
            #     player_flee_button.draw(screen)

            self.screen.fill(BLACK)
            self.map.run()
            if self.map.player.health <= 0:
                running = False
            pygame.display.update()
            self.clock.tick(FPS)

    def game_over(self):
        title_font = pygame.font.SysFont("inkfree", 115)
        font = pygame.font.SysFont("inkfree", 40)
        game_over_text = title_font.render('GAME OVER', True, RED)
        backspace_caption = font.render('-Backspace to EXIT game-', True, GRAY) #magenta

        play = True
        while play:
            self.screen.fill(BLACK)
            self.screen.blit(game_over_text, (120, 100))
            self.screen.blit(backspace_caption, (180, 350))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_BACKSPACE:
                        play = False
                        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.homescreen()
    game.run()
    game.game_over()