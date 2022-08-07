import pygame
import configparser
from pathlib import Path
from constants import *
import collections


class ChessGame():
    def __init__(self, database=None):
        # Initialize game
        pygame.display.init()
        pygame.font.init()


        # Initialize game settings
        self.settings = self.load_settings()
        self.set_difficulty(self.settings['Game']['Difficulty'])

        # Initialize database
        self.database = self.load_database(database)


    def __load_settings(self):
        parser = configparser.RawConfigParser()
        parser.read(GAMEOPTIONS)

        section_dict = collections.defaultdict()
        for section in parser.sections():
            section_dict[section] = dict(parser.items(section))
    
        return section_dict


    def _set_difficulty(self, difficulty: str) -> None:
        rating = {"easy": 800, "normal": 1100, "hard": 1400}    # Set difficulty rating for puzzles

        if difficulty not in rating.keys():
            raise ValueError(f"Invalid Difficulty: {difficulty}")
        
        self.rating = rating[difficulty]


    def _set_game_type(self, game_type):
        if game_type not in ['normal', 'puzzle']:
            raise ValueError(f"Invalid Game Type: {game_type}")

        self.game_type = game_type
    

    
    def _load_database(self, database):
        if not database:
            return PuzzleDatabase()
        
        return PuzzleDatabase(database=database)
