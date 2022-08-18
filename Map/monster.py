import pygame
import random
import pathlib

from .support import import_folder

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
SCALING_FACTOR = 2.5
DEFAULT_IMAGE_SIZE = (16 * SCALING_FACTOR, 28 * SCALING_FACTOR)
class Monster(pygame.sprite.Sprite):
    def __init__(self, position, groups, obstacle_sprites, level=1, hp=20):
        super().__init__(groups)
        self.level = level
        self.hp = hp
        self.image = pygame.image.load(pathlib.Path(__file__).parent.parent / 'Graphics-Audio/lizard_monster.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = position)

        self.health = hp
        self.paces_to_turn = 20
        self.pace_count = 0
        self.direction = 1
        self.speed = 1
        self.status = "right"
        self.animation_speed = 0.15
        self.frame_index = 0

        self.obstacle_sprites = obstacle_sprites
        self.import_monster_assets()

    def __str__(self):
        return f'Monster - Level: {self.level} Health: {self.hp}'

    def __repr__(self):
        return f'Monster(level={self.level}, hp={self.hp})'

    def import_monster_assets(self):
        player_path = pathlib.Path(__file__).parent.parent / 'Graphics-Audio/monster/'
        self.animations = {'right': [], 'left': []}
        for animation in self.animations.keys():
            full_path = player_path / animation
            self.animations[animation] = import_folder(full_path)
        print(self.animations)

    def animate(self):
        animation = self.animations[self.status]
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
        if animation:
            self.image = pygame.transform.scale( animation[int(self.frame_index)], DEFAULT_IMAGE_SIZE)

    def attack(self, other):
        attack_damage = random.choice(range(self.level, self.level + 3))
        print("Hero took " + str(attack_damage) + " damage")
        other.health -= attack_damage

    def get_health(self):
        self.health -= 5
        # need a bar or something to show monster health or something
        self.check_death()
        
    def check_death(self):
        if self.health <= 0:
            self.kill()
        else:
            pass

    def update(self):
        self.check_death()
        self.animate()
        self.move()
    def move(self):
        self.rect.x += self.direction * self.speed
        self.pace_count += 1
        self.speed = 1
        direction_status = {1: "right", -1: "left"}
        if self.collide():
            self.direction *= -1
            self.status = direction_status[self.direction]
            self.pace_count = 0

    def collide(self):
        collided_sprites = pygame.sprite.spritecollide(self, self.obstacle_sprites, False)
        for sprite in collided_sprites:
            # Janky fix - circular import
            foobar = getattr(sprite, 'hero_type', None)     # checks if object has attribute
            if callable(foobar):                            # checks if the attribute is callable
                if "attack" in sprite.status:
                    self.get_health()
                else:
                    self.attack(sprite)
        if len(collided_sprites) > 1:
            return True
