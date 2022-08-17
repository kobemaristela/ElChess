import pygame
from .constants import *
from .puzzles.fenparser import FenParser


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
    

    def load_puzzle(self, puzzle):
        if not puzzle:
            return None, None

        temp_puzzle = puzzle.split(',')
        puzzle = FenParser(temp_puzzle[0], game=True)

        return puzzle, temp_puzzle[1].split(" ")


    def get_board_coordinates(self):
        board_coordinates = []
        for x in range(0, 8):
            board_coordinates.append([])    # Row
            for y in range(0, 8):
                board_coordinates[x].append([(x * self.square_size), 
                                                (y * self.square_size)])    # Column
        
        return board_coordinates


    def load_chess_pieces(self):
        chess_pieces = {"w": {'K': WHITEKING, 'Q':WHITEQUEEN, 'B':WHITEBISHOP, 'N':WHITEKNIGHT, 'R':WHITEROOK, 'P':WHITEPAWN},
                        "b": {'k': BLACKKING, 'q':BLACKQUEEN, 'b':BLACKBISHOP, 'n':BLACKKNIGHT, 'r':BLACKROOK, 'p':BLACKPAWN}}

        for side in chess_pieces.keys():
            for piece in chess_pieces[side].keys():
                chess_pieces[side][piece] = pygame.transform.scale(pygame.image.load(chess_pieces[side][piece]), (self.square_size, self.square_size))

        return chess_pieces


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



    def main(self):
        # Initualize board
        self.setup_board()

        
        # Setup Trackers
        selected_pieces = []
        print(self.solution)
        print(self.puzzle.get_board())

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    loc = pygame.mouse.get_pos()

                    # Get board coordinates
                    col, row = (loc[0] // self.square_size), (loc[1] // self.square_size)
                    board_piece = self.puzzle.get_board_piece(row,col)


                    # Logic check - Moving Active Color Piece
                    if not selected_pieces and (board_piece == " " or \
                        (self.puzzle.active == 'w' and not board_piece.isupper()) or \
                        (self.puzzle.active == 'b' and not board_piece.islower())):

                        continue

                    
                    # Clear if same piece was last selected
                    selected_pieces.clear() if len(selected_pieces) > 1 or (row,col) in selected_pieces else selected_pieces.append((row,col))
                    
                    if len(selected_pieces) == 2:
                        board_move = f"{BOARDUCI[selected_pieces[0][0]][selected_pieces[0][1]]}{BOARDUCI[selected_pieces[1][0]][selected_pieces[1][1]]}"
                        move = FenParser.convert_uci_move(board_move)
                        print(self.puzzle.get_legal_moves())
                        print(self.solution[0])
                        print(move)

                        if move not in self.puzzle.get_legal_moves() or board_move != self.solution[0]:
                            print("Incorrect Move... Try Again")
                            selected_pieces.clear()
                            continue
                        

                        
                        print("Correct Move")
                        

                        



            self.clock.tick(20)
            pygame.display.flip()


if __name__ == "__main__":
    chess_board = ChessBoard()
    chess_board.main()