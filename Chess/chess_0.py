import pygame
from pathlib import Path
from board_constants import *

class Chess1:
    def __init__(self) -> None:
        # Initialize game
        pygame.display.init()
        pygame.font.init()
        
        # Game Assets
        self.assets = CURRENTDIRECTORY.joinpath('assets')
        
        # Board
        self.board = pygame.image.load(self.assets.joinpath('board.png')).convert()
        self.board_coordinates = []
        
        # Set Properties
        pygame.display.set_caption("ElChess")
        
        
        self.window = pygame.display.set_mode([600, 900])
        
        pygame.display.flip()
        
    
    def main(self):
        self.board_offset_x = 0
        self.board_offset_y = 50
        self.board_dimensions = (self.board_offset_x, self.board_offset_y)
        

    # def move_piece(self, move):
        


    def get_board_coordinates(self):
        length = self.board_img.get_rect().width // 8
        for x in range(0, 8):
            self.board_coordinates.append([])
            for y in range(0, 8):
                self.board_locations[x].append([self.board_offset_x + (x * length), 
                                                self.board_offset_y + (y * length)])
