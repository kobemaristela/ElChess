import pygame, sys
from map_constants import *

class Player_UI:
    def __init__(self):
        self.display_surf = pygame.display.get_surface()
        self.health_bar_image = pygame.Rect(10, 10, HEALTH_BAR_WIDTH, HEALTH_BAR_HEIGHT)
        self.health_font = pygame.font.SysFont("inkfree", 12)

    def display_health_bar(self, player):
        pygame.draw.rect(self.display_surf, BLACK, self.health_bar_image)
    