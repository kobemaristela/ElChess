import pygame
import random
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
    def __init__(self, position, groups, name, level=1, hp=3, health=100):
        super().__init__(groups)
        self.image = pygame.image.load('./Graphics-Audio/knight_player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = position)

        self.direction = pygame.math.Vector2()
        self.speed = 3
        self.health = health
        self.name = name
        self.level = level
        self.hp = hp
        
    
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

    def health_scale(self, health):

        return