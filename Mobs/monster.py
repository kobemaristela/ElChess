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


class Monster(pygame.sprite.Sprite):
    def __init__(self, x, y, level=1, hp=1):
        super(Monster, self).__init__()
        self.level = level
        self.hp = hp
        self.surf = pygame.Surface((50, 50))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(center=(x, y))
    
    def __str__(self):
        return f'Monster - Level: {self.level} Health: {self.hp}'

    def __repr__(self):
        return f'Monster(level={self.level}, hp={self.hp})'

    def attack(self, other):
        attack_damage = random.choice(range(self.level, self.level + 3))
        other.hp -= attack_damage