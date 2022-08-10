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
        
        self.obstacle_sprites = obstacle_sprites
    
    def __str__(self):
        return f'Hero {self.name} - Level: {self.level} Health: {self.hp}'

    def __repr__(self):
        return f'Hero(name={self.name}, level={self.level}, hp={self.hp})'
    
    def attack(self, other):
        attack_damage = random.choice(range(self.level + 2, self.level + 5))
        other.hp -= attack_damage

    
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
    
    def import_player_assets(self):
        player_path = pathlib.Path(__file__).parent.parent / 'Graphics-Audio/player/'
        self.animations = {'right_idle': [], 'left_idle': [], 'up_idle': [], 'down_idle': [], 
                            'right': [], 'left': [], 'up': [], 'down': []}
        for animation in self.animations.keys():
            full_path = player_path / animation
            self.animations[animation] = import_folder(full_path)
        print(self.animations)
    
    def get_status(self):
        if self.direction.x == 0 and self.direction.y == 0:
            if 'idle' not in self.status:
                self.status += '_idle'
    
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
        collided_sprites = pygame.sprite.spritecollide(self, self.obstacle_sprites, False, custom_collide)
        for sprite in collided_sprites:
            #could potentially handle monster battles below
            if type(sprite) == Monster:
                # print("monster collision\n")
                self.health -= 0.5
                sprite.hp -= 0.1
                if sprite.hp < 0:
                    sprite.kill()
            elif direction == "horizontal":
                if self.direction.x > 0:
                    self.rect.right = sprite.rect.left - PADDING_CONST
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

#fixes overlap collision
def custom_collide(hero_sprite: Hero, sprite: pygame.sprite.Sprite) -> bool:
    collision_rect = pygame.rect.Rect(sprite.rect.left - PADDING_CONST, sprite.rect.top, sprite.rect.width + PADDING_CONST,sprite.rect.height)
    return collision_rect.colliderect(hero_sprite.rect)