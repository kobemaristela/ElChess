from multiprocessing import freeze_support
from RPG.rpg_game import Game
from ChessGame.chessgame import ChessGame



def start_el_chess():
    el_chess = Game()
    el_chess.homescreen()
    el_chess.run()


def start_chess_game(type):
    game = ChessGame()
    game.set_game_type(type)
    game.main()
    
    
def start_game(selection):
    return {
        'puzzle': lambda: start_chess_game('puzzle'),
        'rpg': lambda: start_el_chess(),
        'chessgame': start_chess_game('game')
    }[selection]()
    

if __name__ == "__main__":
    freeze_support()    # Windows support on multiprocessing
    
    selection = ChessGame.load_settings()['Game']['mode']
    
    try:
        start_game(selection)
    except KeyError:
        print(f"Invalid selection {selection}... \nSupported Game Modes: rpg, puzzle, and chessgame")