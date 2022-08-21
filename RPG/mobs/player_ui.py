import pygame
from pygame.locals import *
from RPG.map_constants import *

class Player_UI:
    def __init__(self):
        self.display_surf = pygame.display.get_surface()
        self.health_bg_rect = pygame.Rect(5, 5, BG_WIDTH, BG_HEIGHT)
        self.health_bar_image = pygame.Rect(10, 10, HEALTH_BAR_WIDTH, HEALTH_BAR_HEIGHT)
        self.health_font = pygame.font.SysFont("microsoftjhengheimicrosoftjhengheiuibold", 18)

    def display_health_bar(self, player, curr_health, max_health):
        pygame.draw.rect(self.display_surf, BLACK, self.health_bar_image)
        pygame.draw.rect(self.display_surf, WHITE, self.health_bg_rect)

        health_ratio = curr_health / max_health
        width_of_curr = self.health_bar_image.width * health_ratio
        curr_health_rect = self.health_bar_image.copy()
        curr_health_rect.width = width_of_curr

        self.health_text = self.health_font.render('Health', True, RED)

        pygame.draw.rect(self.display_surf, RED, curr_health_rect, curr_health_rect.width)
        self.display_surf.blit(self.health_text, (120, 16))

    def get_health_status(self):
        pass