import pygame, sys
from pygame.locals import *
import pathlib
from map_constants import *
from hero import Hero
from monster import Monster
from player_ui import Player_UI

class Wall(pygame.sprite.Sprite):
    def __init__(self, position, groups, type):
        super().__init__(groups)
        if type == 'mid':
            self.image = pygame.image.load(pathlib.Path(__file__).parent.parent / 'Graphics-Audio/wall_mid.png').convert_alpha()
        elif type == 'left':
            self.image = pygame.image.load(pathlib.Path(__file__).parent.parent / 'Graphics-Audio/wall_left.png').convert_alpha()
        elif type == 'right':
            self.image = pygame.image.load(pathlib.Path(__file__).parent.parent / 'Graphics-Audio/wall_right.png').convert_alpha()
        elif type == 'goo':
            self.image = pygame.image.load(pathlib.Path(__file__).parent.parent / 'Graphics-Audio/wall_goo.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = position)
        
        #fixes issue with player being unable to reach left walls
        if type == "left":
            self.rect.width //= 3
        
class Door(pygame.sprite.Sprite):
   def __init__(self, position, groups):
        super().__init__(groups)
        self.image = pygame.image.load(pathlib.Path(__file__).parent.parent / 'Graphics-Audio/door.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = position)

class Boss(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)
        self.image = pygame.image.load(pathlib.Path(__file__).parent.parent / 'Graphics-Audio/boss_pic.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = position)

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

class Map:
    def __init__(self):
        self.display_screen = pygame.display.get_surface()

        self.visible_sprites = Player_Camera()
        self.obstacle_sprites = pygame.sprite.Group()
        self.monster_collideables = pygame.sprite.Group() #group includes Monsters, Walls, and Hero
        self.make_map()

        #player UI
        self.player_ui = Player_UI()

    def make_map(self):
        for row_index, row in enumerate(RPG_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE
                if col == 'w':
                    Wall((x, y), [self.visible_sprites, self.obstacle_sprites,self.monster_collideables], 'mid')
                elif col == 'l':
                    Wall((x, y), [self.visible_sprites, self.obstacle_sprites,self.monster_collideables], 'left')  
                elif col == 'r':
                    Wall((x, y), [self.visible_sprites, self.obstacle_sprites,self.monster_collideables], 'right')
                elif col == 'g':
                    Wall((x, y), [self.visible_sprites, self.obstacle_sprites,self.monster_collideables], 'goo')
                elif col == 'd':
                    Door((x, y), [self.visible_sprites, self.obstacle_sprites,self.monster_collideables])           
                elif col == 'p':
                    self.player = Hero((x, y), [self.visible_sprites, self.monster_collideables],'bob', self.obstacle_sprites)
                elif col == 'B':
                    Boss((x, y), [self.visible_sprites, self.obstacle_sprites, self.monster_collideables])
                elif col == 'M':
                    Monster((x, y), [self.visible_sprites, self.obstacle_sprites, self.monster_collideables], self.monster_collideables)
                
    def run(self):
        self.visible_sprites.center_camera_draw(self.player)
        self.visible_sprites.update()
        self.player_ui.display_health_bar(self.player, self.player.health, 100)

class Player_Camera(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_screen = pygame.display.get_surface()
        self.vector_to_keep_player_center = pygame.math.Vector2()

        # instantiate floor
        self.floor_surf = pygame.image.load(pathlib.Path(__file__).parent.parent / 'Graphics-Audio/Floor.png').convert()
        self.floor_rect = self.floor_surf.get_rect(topleft = (0, 0))

    def center_camera_draw(self, player):
        self.vector_to_keep_player_center.x = player.rect.centerx - (WIDTH // 2)
        self.vector_to_keep_player_center.y = player.rect.centery - (HEIGHT // 2)

        floor_pos = self.floor_rect.topleft - self.vector_to_keep_player_center
        self.display_screen.blit(self.floor_surf, floor_pos)

        for sprite in self.sprites():
            camera_position = sprite.rect.topleft - self.vector_to_keep_player_center
            self.display_screen.blit(sprite.image, camera_position)