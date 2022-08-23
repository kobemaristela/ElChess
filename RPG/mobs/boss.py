import pygame

from RPG.map_constants import *
from RPG.support import import_folder 


SCALING_FACTOR = 2.5
DEFAULT_IMAGE_SIZE = (32 * SCALING_FACTOR, 32 * SCALING_FACTOR)

class Boss(pygame.sprite.Sprite):
    def __init__(self, position, groups, obstacle_sprites):
        super().__init__(groups)
        self.image = pygame.image.load(ASSETS_MONSTER.joinpath('boss.png')).convert_alpha()
        self.rect = self.image.get_rect(topleft = position)
        self.obstacle_sprites = obstacle_sprites
        self.import_boss_assets()
        self.direction = 1
        self.speed = 1
        self.status = "right"
        self.animation_speed = 0.15
        self.frame_index = 0

    def import_boss_assets(self):
        self.animations = {'right': [], 'left': []}
        for animation in self.animations.keys():
            full_path = ASSETS_BOSS / animation
            self.animations[animation] = import_folder(full_path)
        print("Boss animations:")
        print(self.animations)
    
    def move(self):
        self.rect.x += self.direction * self.speed
        self.speed = 1
        direction_status = {1: "right", -1: "left"}
        if self.collide():
            self.direction *= -1
            self.status = direction_status[self.direction]

    def collide(self):
        collided_sprites = pygame.sprite.spritecollide(self, self.obstacle_sprites, False)
        if len(collided_sprites) > 1:
            return True
        return False

    def animate(self):
        animation = self.animations[self.status]
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
        if animation:
            self.image = pygame.transform.scale( animation[int(self.frame_index)], DEFAULT_IMAGE_SIZE)
    def update(self):
        self.animate()
        self.move()