import pygame
from pathlib import Path
from constants import *


class ChessGame():
    def __init__(self, type, difficulty, ):
        # Initialize game
        pygame.display.init()
        pygame.font.init()



        #

    def set_difficulty(self, difficulty: str) -> None:
        rating = {"easy": 800, "normal": 1100, "hard": 1400}
        
        if difficulty not in rating.keys():
            raise ValueError("Invalid Difficulty: Only accept easy, normal, and hard")
        
        self.rating = rating[difficulty]