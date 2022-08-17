from Map.rpg_game import Game
from ChessGame.chessgame import ChessGame
import multiprocessing as mp

# Test Driver
MERGEATTEMPT = False


if MERGEATTEMPT:
    game = Game()
    game.homescreen()
    game.run()  
else:
    chess = ChessGame()
    chess.set_game_type('puzzle')
    chess.main()

