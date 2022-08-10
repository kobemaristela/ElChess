import pygame
import random
import pathlib

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
    def __init__(self, position, groups, obtscle_sprites, level=1, hp=20):
        super().__init__(groups)
        self.level = level
        self.hp = hp
        self.image = pygame.image.load(pathlib.Path(__file__).parent.parent / 'Graphics-Audio/lizard_monster.png').convert_alpha()
        #self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(topleft = position)
        self.paces_to_turn = 20
        self.pace_count = 0
        self.direction = 1
        self.speed = 1

        self.obstacle_sprites = obtscle_sprites

    def __str__(self):
        return f'Monster - Level: {self.level} Health: {self.hp}'

    def __repr__(self):
        return f'Monster(level={self.level}, hp={self.hp})'

    def attack(self, other):
        attack_damage = random.choice(range(self.level, self.level + 3))
        other.hp -= attack_damage

    def move(self):
        self.rect.x += self.direction * self.speed
        self.pace_count += 1
        self.speed = 1
        if self.collide():
            self.direction *= -1
            self.pace_count = 0
    def update(self) -> None:
        self.move()
    def collide(self):
        collided_sprites = pygame.sprite.spritecollide(self, self.obstacle_sprites, False)
        if len(collided_sprites) > 1:
            print(collided_sprites)
            return True
