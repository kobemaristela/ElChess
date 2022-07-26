import pygame
from map_constants import *

class Wall(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)
        self.image = pygame.image.load('wall_mid.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = position)

class Player(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)
        self.image = pygame.image.load('knight_player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = position)

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
                    Player((x, y), [self.visible_sprites])
                
    def run(self):
        self.visible_sprites.draw(self.display_screen)