# from Map.rpg_game import Game
from ChessGame.chessgame import ChessGame
import multiprocessing as mp

# Test Driver
# mp.freeze_support()
MERGE = False


# if MERGE == True:
#     game = Game()
#     game.homescreen()
#     game.run()  
# else:
chess = ChessGame()
chess.set_game_type('puzzle')
chess.main()

