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


class Monster(pygame.sprite.Sprite):
    def __init__(self, position, groups, level=1, hp=1):
        super().__init__(groups)
        self.level = level
        self.hp = hp
        self.image = pygame.image.load('./Graphics-Audio/lizard_monster.png').convert_alpha()
        #self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(topleft = position)
    
    def __str__(self):
        return f'Monster - Level: {self.level} Health: {self.hp}'

    def __repr__(self):
        return f'Monster(level={self.level}, hp={self.hp})'

    def attack(self, other):
        attack_damage = random.choice(range(self.level, self.level + 3))
        other.hp -= attack_damage
