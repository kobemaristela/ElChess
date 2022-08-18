import pygame

from RPG.map_constants import * 

class Boss(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)
        self.image = pygame.image.load(ASSETS_MONSTER.joinpath('boss.png')).convert_alpha()
        self.rect = self.image.get_rect(topleft = position)