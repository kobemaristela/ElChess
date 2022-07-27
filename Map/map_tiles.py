from importlib.resources import path
import pygame
from map_constants import *

class Wall(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)
        self.image = pygame.image.load('wall_mid.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = position)

class Boss(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)
        self.image = pygame.image.load('boss_pic.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = position)

class Player(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)
        self.image = pygame.image.load('knight_player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = position)

        self.direction = pygame.math.Vector2()
        self.speed = 3

    def keyboard_input(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_UP]:
            self.direction.y = -1
        elif key_pressed[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0
        
        if key_pressed[pygame.K_RIGHT]:
            self.direction.x = 1
        elif key_pressed[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        self.rect.center += self.direction * speed

    def update(self):
        self.keyboard_input()
        self.move(self.speed)

class Map:
    def __init__(self):
        self.display_screen = pygame.display.get_surface()

        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()
        self.make_map()

    def make_map(self):
        for row_index, row in enumerate(RPG_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE
                if col == 'w':
                    Wall((x, y), [self.visible_sprites, self.obstacle_sprites])
                elif col == 'p':
                    self.player = Player((x, y), [self.visible_sprites])
                elif col == 'B':
                   Boss((x, y), [self.visible_sprites, self.obstacle_sprites])
                
    def run(self):
        self.visible_sprites.draw(self.display_screen)
        self.visible_sprites.update()