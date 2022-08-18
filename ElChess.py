from multiprocessing import freeze_support
from RPG.rpg_game import Game

if __name__ == "__main__":
    freeze_support()    # Windows support on multiprocessing
    
    game = Game()
    game.homescreen()
    game.run()  