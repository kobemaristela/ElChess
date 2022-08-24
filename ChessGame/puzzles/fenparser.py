from itertools import chain
from ChessGame.constants import *
import re
import chess
import chess.engine


class FenParser():
    def __init__(self, fen, game=False):
        self.fen = fen
        self.game = game

        self.pieces = None              # Describes piece placement on board; starts with rank 8 to 1
        self.active = None              # 'w' - white move | 'b' - black move
        self.castling = None            # "K|Q" White castle; "k|q" Black castle
        self.en_passant = None          # Square over which a pawn has just passed while moving two squares
        self.halfmove_clock = None      # Number of halfmoves since the last capture or pawn advance (used for the fifty-move rule)
        self.fullmove_number = None     # Number of full moves

        self.__read_fen()


    def __read_fen(self):
        (self.pieces, self.active, self.castling, self.en_passant,
            self.halfmove_clock, self.fullmove_number) = self.fen.split(' ')
        self.__validate_fen_field()

        if self.game:
            self.game = chess.Board(self.fen)
        

    def __validate_fen_field(self):
        re_pieces = re.compile('^[KkQqBbNnRrPp1-8/]+$')
        re_castle = re.compile('^[KQkq-]+$')
        re_en_passant = re.compile('^[a-h1-8-]+$')
        re_digits = re.compile('^[0-9]*$')

        if not re_pieces.match(self.pieces):
            raise ValueError(f'Invalid pieces: {self.pieces}')
        if self.active not in ('w', 'b'):
            raise ValueError(f'Invalid color: {self.active}')
        if not re_castle.match(self.castling):
            raise ValueError(f'Invalid castling: {self.castling}')
        if not re_en_passant.match(self.en_passant):
            raise ValueError(f'Invalid en passant: {self.en_passant}')
        if not re_digits.match(self.halfmove_clock):
            raise ValueError(f'Invalid halfmove clock: {self.halfmove_clock}')
        if not re_digits.match(self.fullmove_number):
            raise ValueError(f'Invalid fullmove number: {self.fullmove_number}')          


    def __flatten(self, lst):
        return list(chain(*lst))


    def __expand(self, pieces):
        reg_exp = re.compile("(^[KkQqBbNnRrPp]$)")
        res = ""
        if reg_exp.match(pieces):
            res = pieces
        else:
            res = self.__padding(pieces)    # pads spaces
        return res


    def __padding(self, num):
        return int(num) * " "


    def __parse_rank(self, rank):
        reg_exp = re.compile("(\d|[KkQqBbNnRrPp])")
        matches = reg_exp.findall(rank)
        pieces = self.__flatten(map(self.__expand, matches))
        return pieces


    def __update_board(self, fen):
        (self.pieces, self.active, self.castling, self.en_passant,
        self.halfmove_clock, self.fullmove_number) = fen.split(' ')
    
        self.__validate_fen_field()
    
    
    def start_chess_engine(self):
        self.engine = chess.engine.SimpleEngine.popen_uci(STOCKFISH_ENGINE)
        
    
    def make_enemy_move(self):
        if not hasattr(self, "engine"):
            self.__start_chess_engine()
        
        result = self.engine.play(self.game, chess.engine.Limit(time=.1))
        self.game.push(result.move)
        
        self.__update_board(self.game.fen())


    def stop_chess_engine(self):
        if hasattr(self, 'engine') and self.engine: # Short circuit
            self.engine.quit()
        
        
    def reset_board(self):
        self.game = True
        self.__read_fen()


    def parse(self):
        ranks = self.pieces.split("/")
        return [self.__parse_rank(rank) for rank in ranks]


    def get_board_piece(self,row,col):
        return self.parse()[row][col]


    def search_piece(self, piece):
        re_pieces = re.compile(f"^[{piece}1-8/]+$")
        res = re_pieces.match(self.pieces)
        return True if res else False
        
        
    def set_chess_move(self, move):
        self.game.push(move)
        
        self.__update_board(self.game.fen())
        
        
    def get_legal_moves(self):
        return self.game.legal_moves


    def get_board(self):
        return self.game

    
    @staticmethod
    def convert_uci_move(board_move):
        return chess.Move.from_uci(board_move)