from multiprocessing import freeze_support
from Map.rpg_game import Game
from ChessGame.chessgame import ChessGame

# Test Driver
MERGEATTEMPT = False

if __name__ == "__main__":
    freeze_support()    # Windows is stupid
    
    if MERGEATTEMPT:
        game = Game()
        game.homescreen()
        game.run()  
    else:
        chess = ChessGame()
        chess.set_game_type('puzzle')
        chess.main()