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

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

class Hero(pygame.sprite.Sprite):
    def __init__(self, name, level=1, hp=3):
        super(Hero, self).__init__()
        self.name = name
        self.level = level
        self.hp = hp
        self.surf = pygame.Surface((50, 50))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
    
    def __str__(self):
        return f'Hero {self.name} - Level: {self.level} Health: {self.hp}'

    def __repr__(self):
        return f'Hero(name={self.name}, level={self.level}, hp={self.hp})'
    
    def attack(self, other):
        attack_damage = random.choice(range(self.level + 2, self.level + 5))
        other.hp -= attack_damage

    
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -10)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 10)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-10, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(10, 0)
        
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
