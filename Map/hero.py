import pygame
import random
import os
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


class Hero(pygame.sprite.Sprite):
    def __init__(self, position, groups, name, obstacle_sprites, level=1, hp=3):
        super().__init__(groups)
        self.image = pygame.image.load(os.pardir + '/Graphics-Audio/knight_player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = position)

        self.hitbox = self.rect
        self.import_player_assets()
        self.status = 'right'
        self.frame_index = 0
        self.animation_speed = 0.15

        self.direction = pygame.math.Vector2()
        self.speed = 3

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
        player_path = './Graphics-Audio/player/'
        self.animations = {'right_idle': [], 'left_idle': [], 'up_idle': [], 'down_idle': [], 
                            'right': [], 'left': [], 'up': [], 'down': []}
        for animation in self.animations.keys():
            full_path = player_path + animation
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
        self.rect = self.image.get_rect(center=self.hitbox.center)
    
    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        self.rect.x += self.direction.x * speed
        self.collision("horizontal")
        self.rect.y += self.direction.y * speed
        self.collision("vertical")


        self.hitbox.x += self.direction.x * speed
        self.hitbox.y += self.direction.y * speed



    def collision(self, direction):
        collided_sprites = pygame.sprite.spritecollide(self, self.obstacle_sprites, False)
        for sprite in collided_sprites:
            if direction == "horizontal":
                if self.direction.x > 0:
                    self.rect.right = sprite.rect.left
                if self.direction.x < 0:
                    self.rect.left = sprite.rect.right
            if direction == "vertical":
                if self.direction.y > 0:
                    self.rect.bottom = sprite.rect.top
                if self.direction.y < 0:
                    self.rect.top = sprite.rect.bottom
        



    def update(self):
        self.keyboard_input()
        self.get_status()
        self.move(self.speed)