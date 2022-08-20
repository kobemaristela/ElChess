import pygame
import sys
from .constants import *
from .puzzles.fenparser import FenParser
from .sprites.play_button import PlayButton


class ChessBoard:
    def __init__(self, puzzle=None):
        # Initialize variables
        self.screen_width = 750
        self.screen_height = 750

        # Initialze puzzle
        self.puzzle, self.solution = self.load_puzzle(puzzle)

        # Initialize game
        pygame.display.init()
        pygame.font.init()
        
        
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
    

    def load_puzzle(self, puzzle):
        if not puzzle:
            return None, None

        temp_puzzle = puzzle.split(',')
        puzzle = FenParser(temp_puzzle[0], game=True)

        return puzzle, temp_puzzle[1].split(" ")


    def get_board_coordinates(self):
        board_coordinates = []
        for x in range(0, 8):
            board_coordinates.append([])
            for y in range(0, 8):
                board_coordinates[x].append([(x * self.square_size) + 5, 
                                                (y * self.square_size) + 5]) 
        
        return board_coordinates


    def load_chess_pieces(self):
        chess_pieces = {"w": {'K': WHITEKING, 'Q':WHITEQUEEN, 'B':WHITEBISHOP, 'N':WHITEKNIGHT, 'R':WHITEROOK, 'P':WHITEPAWN},
                        "b": {'k': BLACKKING, 'q':BLACKQUEEN, 'b':BLACKBISHOP, 'n':BLACKKNIGHT, 'r':BLACKROOK, 'p':BLACKPAWN}}

        for side in chess_pieces.keys():
            for piece in chess_pieces[side].keys():
                chess_pieces[side][piece] = pygame.transform.scale(pygame.image.load(chess_pieces[side][piece]), (self.square_size, self.square_size))

        return chess_pieces


    def make_chess_move(self, player_move):
        self.puzzle.set_chess_move(player_move)
        self.solution.pop(0)
        
        enemy_move = FenParser.convert_uci_move(self.solution[0])
        self.puzzle.set_chess_move(enemy_move)
        self.solution.pop(0)
        
        self.setup_board()  # Update Board


    def setup_board(self):
        self.window.blit(self.board, (0,0))
        pygame.display.flip()   # Update window

        for ind_r, row in enumerate(self.puzzle.parse()):
            for ind_c, piece in enumerate(row):
                    if piece == " ":
                        continue

                    color = 'w' if piece.isupper() else 'b'
                    self.window.blit(self.chess_pieces[color][piece], self.board_coordinates[ind_c][ind_r])
                
                    pygame.display.flip()   # Update window
    
    
    def highlight_square(self, selected_pieces):
        highlight = pygame.Surface((self.square_size, self.square_size))
        
        highlight.set_alpha(100) # Set transparency
        highlight.fill(pygame.Color("green")) # Set color
        
        self.window.blit(highlight, self.board_coordinates[selected_pieces[1]][selected_pieces[0]]) # Highlight board piece
        
        pygame.display.flip() # Update window
        
        
    def clear_highlight(self, selected_pieces):
        selected_pieces.clear()
        self.setup_board()
        
        
    def init_game_start(self):
        isPause = True
        color = "White's Move" if self.puzzle.active == 'w' else "Black's Move"
        play_button = PlayButton(color, 375, 375, 200, 100, isPause)
        
        while isPause:
            for event in pygame.event.get():
                play_button.handle_event(event)

            play_button.update()

            self.window.fill(BLACK)

            play_button.draw(self.window)

            pygame.display.update()

            self.clock.tick(25)
        

    def main(self):
        # Initialize board
        self.setup_board()
        
        # Setup Trackers
        selected_pieces = []
        isRunning = True    # Game Loop

        while isRunning:
            for event in pygame.event.get():
                if not self.solution:
                    self.running = False
                    print("Boss Defeated")
                    sys.exit()
                    
                if event.type == pygame.QUIT:
                    self.running = False
                    sys.exit()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    loc = pygame.mouse.get_pos()

                    # Get board coordinates
                    col, row = (loc[0] // self.square_size), (loc[1] // self.square_size)
                    board_piece = self.puzzle.get_board_piece(row,col)


                    # Logic check - Moving Active Color Piece
                    if not selected_pieces and (board_piece == " " or \
                        (self.puzzle.active == 'w' and not board_piece.isupper()) or \
                        (self.puzzle.active == 'b' and not board_piece.islower())):
                            
                        if selected_pieces:
                            self.setup_board()
                            
                        selected_pieces.clear()
                            
                        continue

                    
                    # Piece selection logic
                    if len(selected_pieces) > 1 or (row,col) in selected_pieces:
                        self.clear_highlight(selected_pieces)
                        continue
                        
                        
                    selected_pieces.append((row,col))
                    
                    
                    if len(selected_pieces) == 1:
                        self.highlight_square(selected_pieces[0])
                    
                    
                    # Second piece selection
                    if len(selected_pieces) == 2:
                        board_move = f"{BOARDUCI[selected_pieces[0][0]][selected_pieces[0][1]]}{BOARDUCI[selected_pieces[1][0]][selected_pieces[1][1]]}"
                        player_move = FenParser.convert_uci_move(board_move)


                        if player_move not in self.puzzle.get_legal_moves():
                            print("Invalid Move... Try Again")
                            self.clear_highlight(selected_pieces)
                            continue
                        
                        if board_move != self.solution[0]:
                            print("Incorrect Move... Try Again")
                            self.clear_highlight(selected_pieces)
                            continue
                            
                        
                        # Correct Move Handle
                        print("Correct Move")
                        self.highlight_square(selected_pieces[1])   # Highlight correct move
                        self.make_chess_move(player_move)   # Remove move in solution
                        
                        
            self.clock.tick(20)
            pygame.display.flip()