from multiprocessing import freeze_support
from Map.rpg_game import Game
from ChessGame.chessgame import ChessGame

# Test Driver
MERGEATTEMPT = True

if __name__ == "__main__":
    freeze_support()    # Windows is stupid
    
    game = Game()
    game.homescreen()
    game.run()  