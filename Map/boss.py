import pygame
import pathlib

class Boss(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)
        self.image = pygame.image.load(pathlib.Path(__file__).parent.parent / 'Graphics-Audio/boss_pic.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = position)