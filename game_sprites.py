import pygame

from map_constants import BLOCK_SIZE

#thanks to http://programarcadegames.com/index.php?chapter=introduction_to_sprites&lang=en for providing a very useful guide on sprites
class HeroSprite(pygame.sprite.Sprite):

    def __init__(self, color, width, height, initial_pos: tuple):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        
        self.rect = self.image.get_rect()
        self.rect.x = initial_pos[0]
        self.rect.y = initial_pos[1]

class WallSprite(pygame.sprite.Sprite):
    
    def __init__(self, color, width, height, grid_coordinates: tuple):
        super().__init__()

        self.image = pygame.Surface([width,height])
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.x = grid_coordinates[0] * BLOCK_SIZE
        self.rect.y = grid_coordinates[1] * BLOCK_SIZE
