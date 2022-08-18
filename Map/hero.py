import pathlib
import pygame, os
import random
import pathlib
from support import import_folder
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
from monster import Monster
from door import Door

#added to fix collision issue (overlap)
PADDING_CONST = 20

class Hero(pygame.sprite.Sprite):
    def __init__(self, position, groups, name, obstacle_sprites, level=1, hp=3, health=100):
        super().__init__(groups)
        self.image = pygame.image.load(pathlib.Path(__file__).parent.parent / 'Graphics-Audio/knight_player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = position)
        print('\n')
        print(pathlib.Path(__file__).parent.parent / 'Graphics-Audio/knight_player.png')
        self.hitbox = self.rect
        self.import_player_assets()
        self.status = 'right'
        self.frame_index = 0
        self.animation_speed = 0.15

        self.direction = pygame.math.Vector2()
        self.speed = 3
        self.health = health
        self.name = name
        self.level = level
        self.hp = hp
        self.attacking = False
        
        self.obstacle_sprites = obstacle_sprites
    
    def __str__(self):
        return f'Hero {self.name} - Level: {self.level} Health: {self.hp}'

    def __repr__(self):
        return f'Hero(name={self.name}, level={self.level}, hp={self.hp})'

    def keyboard_input(self):

        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_UP]:
            self.direction.y = -1
            self.status = 'up'
        elif key_pressed[pygame.K_DOWN]:
            self.direction.y = 1
            self.status = 'down'
        else:
            self.direction.y = 0
        
        if key_pressed[pygame.K_RIGHT]:
            self.direction.x = 1
            self.status = 'right'
        elif key_pressed[pygame.K_LEFT]:
            self.direction.x = -1
            self.status = 'left'
        else:
            self.direction.x = 0

        # attack input
        if key_pressed[pygame.K_SPACE] and not self.attacking:
            self.attacking = True

            #attack audio
            # self.attack_sound = pygame.mixer.Sound(pathlib.Path(__file__).parent.parent /  'Graphics-Audio/sound-effects/attack_sound.wav')
            # self.attack_sound.set_volume(0.6)
            # self.attack_sound.play()
    
            #attack audio
            # self.attack_sound = pygame.mixer.Sound(pathlib.Path(__file__).parent.parent /  'Graphics-Audio/sound-effects/attack_sound.wav')
            # self.attack_sound.set_volume(0.6)
            # self.attack_sound.play()
    
    def import_player_assets(self):
        player_path = pathlib.Path(__file__).parent.parent / 'Graphics-Audio/player/'
        self.animations = {'right_idle': [], 'left_idle': [], 'up_idle': [], 'down_idle': [],
                            'right_attack': [], 'left_attack': [], 'up_attack': [], 'down_attack': [],
                            'right': [], 'left': [], 'up': [], 'down': []}
        for animation in self.animations.keys():
            full_path = player_path / animation
            self.animations[animation] = import_folder(full_path)
        print(self.animations)
    
    def get_status(self):
        if self.direction.x == 0 and self.direction.y == 0:
            if 'idle' not in self.status and 'attack' not in self.status:
                self.status += '_idle'
        if self.attacking:
            self.direction.x, self.direction.y = 0, 0
            if not 'attack' in self.status:
                if 'idle' in self.status:
                    self.status = self.status.replace('idle', 'attack')
                else:
                    self.status += '_attack'
        else:
            if 'attack' in self.status:
                self.status.replace('_attack', '')
        self.attacking = False
    
    def animate(self):
        animation = self.animations[self.status]
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
        if animation:
            self.image = animation[int(self.frame_index)]
    
    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        self.rect.x += self.direction.x * speed
        self.collision("horizontal")
        self.rect.y += self.direction.y * speed
        self.collision("vertical")

    def collision(self, direction):
        collided_sprites = pygame.sprite.spritecollide(self, self.obstacle_sprites, False, pygame.sprite.collide_rect_ratio(1))
        for sprite in collided_sprites:
            #could potentially handle monster battles below
            if type(sprite) == Monster and "attack" in self.status:
                print('attacking monster')
            elif type(sprite) == Monster:
                print("monster collision\n")
                print(self.attacking)
            elif type(sprite) == Door:
                print('hero collided w/ door')
                Door.move_door(sprite)

            if direction == "horizontal":
                if self.direction.x > 0:
                    self.rect.right = sprite.rect.left
                if self.direction.x < 0:
                    self.rect.left = sprite.rect.right
            elif direction == "vertical":
                if self.direction.y > 0:
                    self.rect.bottom = sprite.rect.top
                if self.direction.y < 0:
                    self.rect.top = sprite.rect.bottom
        
    def update(self):
        self.keyboard_input()
        self.get_status()
        self.animate()
        self.move(self.speed)
#not currently used, but might become useful to fix collisions in the future
def custom_collide(hero_sprite: Hero, sprite: pygame.sprite.Sprite) -> bool:
    collision_rect = pygame.rect.Rect(sprite.rect.left - PADDING_CONST, sprite.rect.top, sprite.rect.width + PADDING_CONST,sprite.rect.height)
    return collision_rect.colliderect(hero_sprite.rect)