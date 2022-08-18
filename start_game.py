from Map.rpg_game import Game
from ChessGame.chessgame import ChessGame

# Test Driver
MERGEATTEMPT = True

if MERGEATTEMPT:
    game = Game()
    game.homescreen()
    game.run()  
else:
    chess = ChessGame()
    chess.set_game_type('puzzle')
    chess.main()

