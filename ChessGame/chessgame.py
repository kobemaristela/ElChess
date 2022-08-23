from configparser import RawConfigParser
from collections import defaultdict
from random import choice
from pathlib import Path

from .constants import *
from .puzzles.puzzledatabase import PuzzleDatabase
from .chessboard import ChessBoard


class ChessGame():
    def __init__(self, database=None, hero=None):
        # Initialize game settings
        self.settings = ChessGame.load_settings()
        self.set_difficulty(self.settings['Game']['difficulty'])

        # Initialize database
        self.database = self.load_database(database)
        self.hero = hero

    @staticmethod
    def load_settings():
        parser = RawConfigParser()
        parser.read(GAMEOPTIONS)

        section_dict = defaultdict()
        for section in parser.sections():
            section_dict[section] = dict(parser.items(section))
    
        return section_dict


    def set_difficulty(self, difficulty: str) -> None:
        rating = {"easy": 800, "normal": 1100, "hard": 1400}    # Set difficulty rating for puzzles

        if difficulty not in rating.keys():
            raise ValueError(f"Invalid Difficulty: {difficulty}")
        
        self.rating = rating[difficulty]


    def set_game_type(self, game_type):
        if game_type not in ['game', 'puzzle']:
            raise ValueError(f"Invalid Game Type: {game_type}")

        self.game_type = game_type
        
        print(self.database)
    
    
    def load_database(self, database):
        db = {'easy': EASY_DATABASE, 'normal': NORMAL_DATABASE, 'hard': HARD_DATABASE}
        if database and Path.exists(database):
            return PuzzleDatabase(database=database)

        if self.settings['Game']['difficulty'] in db.keys():
            return PuzzleDatabase(database=db[self.settings['Game']['difficulty']])
        
        return PuzzleDatabase(database=NORMAL_DATABASE)


    def main(self):
        if not hasattr(self, "game_type"):
            raise ValueError(f"Game type set to {self.game_type}")

        if self.game_type == "puzzle":
            self.database.main(read=True)
            puzzle = choice(self.database.read_results())

            chess = ChessBoard(puzzle, self.hero)
            chess.main()


        if self.game_type == "game":
            chess = ChessBoard()
            chess.main()