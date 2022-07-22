from itertools import chain
import re


class FenParser():
    def __init__(self, fen):
        self.fen = fen

        self.pieces = None              # Describes piece placement on board; starts with rank 8 to 1
        self.active = None              # 'w' - white move | 'b' - black move
        self.castling = None            # "K|Q" White castle; "k|q" Black castle
        self.en_passant = None          # Square over which a pawn has just passed while moving two squares
        self.halfmove_clock = None      # Number of halfmoves since the last capture or pawn advance (used for the fifty-move rule)
        self.fullmove_number = None     # Number of full moves

    def read_fen(self):
        (self.pieces, self.active, self.castling, self.en_passant,
            self.halfmove_clock, self.fullmove_number) = self.fen.split(' ')
        
        self.validate_fen_field()

    def validate_fen_field(self):
        re_castle = re.compile('^[KQkq-]+$')
        re_en_passant = re.compile('^[a-h1-8-]+$')
        re_digits = re.compile('^[0-9]*$')

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

    def parse(self):
        ranks = self.fen.split(" ")[0].split("/")
        rank_pieces = [self.parse_rank(rank) for rank in ranks]
        return rank_pieces

    def parse_rank(self, rank):
        reg_exp = re.compile("(\d|[kqbnrpKQBNRP])")
        matches = reg_exp.findall(rank)
        pieces = self.flatten(map(self.expand, matches))
        return pieces

    def flatten(self, lst):
        return list(chain(*lst))

    def expand(self, pieceString):
        reg_exp = re.compile("([kqbnrpKQBNRP])")
        res = ""
        if reg_exp.match(pieceString):
            res = pieceString
        else:
            res = self.padding(pieceString)
        return res

    def padding(self, num_str):
        return int(num_str) * " "


if __name__ == "__main__":
    FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    p = FenParser(FEN)

    [print(rank) for rank in p.parse()]
