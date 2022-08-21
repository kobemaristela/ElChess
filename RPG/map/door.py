import pygame

from RPG.map_constants import *

class Door(pygame.sprite.Sprite):
    def __init__(self, position, groups, door_status):
        super().__init__(groups)
        self.image = pygame.image.load(ASSETS_DOOR.joinpath('door.png')).convert_alpha()
        self.rect = self.image.get_rect(topleft = position)

        self.door_status = door_status

    def move_door(self):
        if self.door_status == 'closed':
            self.image = pygame.image.load(ASSETS_DOOR.joinpath('doors_open.png')).convert_alpha()
            self.door_status = 'open'
            self.kill()
        elif self.door_status == 'open':
            self.image = pygame.image.load(ASSETS_DOOR.joinpath('door.png')).convert_alpha()
            self.door_status = 'closed'