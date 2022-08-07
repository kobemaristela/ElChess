import pygame
from pathlib import Path
from constants import *


class ChessGame():
    def __init__(self, game_type, difficulty, database=None):
        # Initialize game
        pygame.display.init()
        pygame.font.init()


        # Initialize game settings
        self.set_game_type(game_type)
        self.set_difficulty(difficulty)

        self.database = database


    def set_difficulty(self, difficulty: str) -> None:
        rating = {"easy": 800, "normal": 1100, "hard": 1400}    # Set difficulty rating for puzzles

        if difficulty not in rating.keys():
            raise ValueError(f"Invalid Difficulty: {difficulty}")
        
        self.rating = rating[difficulty]


    def set_game_type(self, game_type):
        if game_type not in ['normal', 'puzzle']:
            raise ValueError(f"Invalid Game Type: {game_type}")

        self.game_type = game_type
    

    def initialize_database(self, database):
        
