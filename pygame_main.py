import random
import pygame
from Mobs.hero import Hero
from Mobs.monster import Monster
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT
)


class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
    
    def draw(self, surface):
        action = False

        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action


class Battle():
    def __init__(self, hero, monster):
        self.hero = hero
        self.monster = monster
        


if __name__ == '__main__':
    pygame.init()
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

    font = pygame.font.Font(None, 64)

    hero = Hero('Bill')
    monster1 = Monster(300, 400)
    monster2 = Monster(600, 300)

    monsters = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    monsters.add(monster1)
    monsters.add(monster2)
    all_sprites.add(monster1)
    all_sprites.add(monster2)
    all_sprites.add(hero)

    attack_button_img = pygame.image.load('attack_button.png').convert_alpha()
    flee_button_img = pygame.image.load('flee_button.png').convert_alpha()
    player_attack_button = Button(50, 450, attack_button_img, 0.65)
    player_flee_button = Button(450, 450, flee_button_img, 0.65)

    clock = pygame.time.Clock()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False
        
        pressed_keys = pygame.key.get_pressed()
        hero.update(pressed_keys)

        screen.fill((50, 90, 200))

        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)
        
        
        monster_to_attack = pygame.sprite.spritecollideany(hero, monsters)
        if monster_to_attack:
            if player_attack_button.draw(screen):
                print(monster_to_attack)
                hero.attack(monster_to_attack)
                print(monster_to_attack)

                if monster_to_attack.hp <= 0:
                    monster_to_attack.kill()
            
            player_flee_button.draw(screen)

        pygame.display.flip()

        clock.tick(30)