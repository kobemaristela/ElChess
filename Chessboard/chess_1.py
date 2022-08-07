# import pygame
from board_constants import *
import chess
import chess.svg

class ChessPuzzle():
    def __init__(self, fen, solution=None) -> None:
        # Initialize variables
        self.fen = fen
        self.solution = solution
        
        self.chess_board = chess.Board(self.fen)
    
        
        # print(self.board)
        # self.board
        

if __name__ == "__main__":
    FEN = "4p3/5pk1/1p3pP1/3p3p/2pP4/P4P1P/1P3PP1/7K w - - 6 34"
    test = ChessPuzzle(FEN)
    
    
    