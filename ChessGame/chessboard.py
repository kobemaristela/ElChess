import pygame
from pathlib import Path
from constants import *
import time

class ChessBoard:
    def __init__(self):
        # Initialize variables
        self.screen_width = 750
        self.screen_height = 750


        # Initialize game
        pygame.display.init()
        pygame.font.init()
        self.running = True # Game loop
        
        
        # Create game window
        self.window = pygame.display.set_mode([self.screen_width, self.screen_height])
        self.clock = pygame.time.Clock()    # Set game clock
        pygame.display.set_caption("ElChess")   # Set Title


        # Board Dimensions
        self.board = pygame.transform.scale(pygame.image.load(BOARD),
                                             (self.screen_width, self.screen_height))
        
        self.square_size = self.board.get_rect().width // 8   # Individual Square Sizes
        self.board_coordinates = self.get_board_coordinates() # Board Spaces


        # Chess Pieces
        self.chess_pieces = self.load_chess_pieces()
        

    def get_board_coordinates(self):
        board_coordinates = []
        for x in range(0, 8):
            board_coordinates.append([])    # Row
            for y in range(0, 8):
                board_coordinates[x].append([(x * self.square_size), 
                                                (y * self.square_size)])    # Column
        
        return board_coordinates


    def load_chess_pieces(self):
        chess_pieces = {"white": {'king': WHITEKING, 'queen':WHITEQUEEN, 'bishop':WHITEBISHOP, 'knight':WHITEKNIGHT, 'rook':WHITEROOK},
                        'black': {'king': BLACKKING, 'queen':BLACKQUEEN, 'bishop':BLACKBISHOP, 'knight':BLACKKNIGHT, 'rook':BLACKROOK}}

        for side in chess_pieces.keys():
            for piece in chess_pieces[side].keys():
                chess_pieces[side][piece] = pygame.transform.scale(pygame.image.load(chess_pieces[side][piece]), (self.square_size, self.square_size))

        return chess_pieces


    def setup_board(self):
        self.window.blit(self.board, (0,0)) # Display Base Board
        pygame.display.flip()   # Update window


        self.window.blit(self.chess_pieces['black']['king'], self.board_coordinates[0][7])
        pygame.display.flip()   # Update window
        self.window.blit(self.chess_pieces['black']['king'], self.board_coordinates[0][6])
        pygame.display.flip()   # Update window


    def main(self):
        self.setup_board()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False


            self.clock.tick(20)
            pygame.display.flip()


if __name__ == "__main__":
    chess_board = ChessBoard()
    chess_board.main()