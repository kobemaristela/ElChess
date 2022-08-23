import pygame
import sys

from RPG.map_constants import GRAY
from RPG.mobs.player_ui import Player_UI
from .constants import *
from .puzzles.fenparser import FenParser
from .sprites.play_button import PlayButton
from pygame import *

class ChessBoard:
    def __init__(self, puzzle=None, hero=None):
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

        self.chessboard_start_screen()


        # Board Dimensions
        self.board = pygame.transform.scale(pygame.image.load(BOARD),
                                             (self.screen_width, self.screen_height))
        
        self.square_size = self.board.get_rect().width // 8   # Individual Square Sizes
        self.board_coordinates = self.get_board_coordinates() # Board Spaces


        # Chess Pieces
        self.chess_pieces = self.load_chess_pieces()

        self.hero = hero
        self.player_ui = Player_UI()

    def load_puzzle(self, puzzle):
        if puzzle is None:
            fen = r'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
            game = FenParser(fen, game=True)
            game.start_chess_engine()
            
            return game, None

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


    def make_enemy_chess_game_move(self):
        # asyncio.set_event_loop_policy(chess.engine.EventLoopPolicy())
        # asyncio.run(self.puzzle.make_enemy_move())
        self.puzzle.make_enemy_move()
        
    
    def make_chess_puzzle_move(self):
        self.solution.pop(0)
        
        enemy_move = FenParser.convert_uci_move(self.solution[0])
        self.puzzle.set_chess_move(enemy_move)
        self.solution.pop(0)


    def make_chess_move(self, player_move):
        self.puzzle.set_chess_move(player_move)
        
        self.make_chess_puzzle_move()  if self.solution is not None else self.make_enemy_chess_game_move()
        
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


    def player_piece(self) -> str:
        if self.puzzle.active == 'w':
            return 'white'
        elif self.puzzle.active == 'b':
            return 'brown'


    def chessboard_start_screen(self):
        piece_str = "You are the " + self.player_piece() + " pieces!"

        title_font = pygame.font.SysFont("inkfree", 70)
        font = pygame.font.SysFont("inkfree", 50)
        chessboard_text = title_font.render('Elchess Boss Battle', True, RED)
        player_color_text = font.render(piece_str, True, WHITE)
        continue_text = font.render('Press anywhere to start', True, GRAY)  

        start_puzzle = True
        while start_puzzle:
            self.window.fill(BLACK)
            self.window.blit(chessboard_text, (80, 100))
            self.window.blit(player_color_text, (100, 300))
            self.window.blit(continue_text, (120, 400)) 
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_BACKSPACE:
                        start_puzzle = False
                        sys.exit()
                elif event.type == MOUSEBUTTONDOWN:
                    start_puzzle = False
                    self.window.fill(BLACK)
                    pygame.display.flip()


    def main(self):
        # Initialize board
        self.setup_board()
        
        # Setup Trackers
        selected_pieces = []
        isRunning = True    # Game Loop

        while isRunning:
            self.player_ui.display_health_bar(self.hero, self.hero.health, 100)
            for event in pygame.event.get():
                if self.solution is not None and len(self.solution) == 0:
                    self.running = False
                    print("Boss Defeated")
                    return
                    
                if event.type == pygame.QUIT:
                    self.running = False
                    self.puzzle.stop_chess_engine()
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
                            print(self.solution[0])
                            continue
                        
                        if self.solution is not None and board_move != self.solution[0]:
                            print("Incorrect Move... Try Again")
                            self.clear_highlight(selected_pieces)
                            if self.hero:
                                self.hero.health -= 5
                                print(self.hero.health)
                            if self.hero.health <= 0:
                                return
                            continue
                            
                        
                        # Correct Move Handle
                        print("Correct Move")
                        self.highlight_square(selected_pieces[1])   # Highlight correct move
                        self.make_chess_move(player_move)   # Remove move in solution
                        
                        
            self.clock.tick(20)
            pygame.display.flip()