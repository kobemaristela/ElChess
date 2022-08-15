from pathlib import Path

# Board UCI
BOARDUCI = [['a8','b8','c8','d8','e8','f8','g8','h8'],
            ['a7','b7','c7','d7','e7','f7','g7','h7'],
            ['a6','b6','c6','d6','e6','f6','g6','h6'],
            ['a5','b5','c5','d5','e5','f5','g5','h5'],
            ['a4','b4','c4','d4','e4','f4','g4','h4'],
            ['a3','b3','c3','d3','e3','f3','g3','h3'],
            ['a2','b2','c2','d2','e2','f2','g2','h2'],
            ['a1','b1','c1','d1','e1','f1','g1','h1']]


# Directory
CURRENTDIRECTORY = Path(__file__).parent.resolve()

GAMEOPTIONS = CURRENTDIRECTORY.parent.joinpath('settings.conf')


## CSV Database
DATABASE_CSV = CURRENTDIRECTORY.joinpath(r'puzzles/database/lichess_db_puzzle.csv')
EASY_DATABASE = CURRENTDIRECTORY.joinpath(r'puzzles/database/easy_db.csv')
NORMAL_DATABASE = CURRENTDIRECTORY.joinpath(r'puzzles/database/normal_db.csv')
HARD_DATABASE = CURRENTDIRECTORY.joinpath(r'puzzles/database/hard_db.csv')

## Chess Board
BOARD = CURRENTDIRECTORY.joinpath(r'assets/board.png')

## White Pieces
WHITEKING = CURRENTDIRECTORY.joinpath(r'assets/chess-king-white.png')
WHITEQUEEN = CURRENTDIRECTORY.joinpath(r'assets/chess-queen-white.png')
WHITEBISHOP = CURRENTDIRECTORY.joinpath(r'assets/chess-bishop-white.png')
WHITEKNIGHT = CURRENTDIRECTORY.joinpath(r'assets/chess-knight-white.png')
WHITEPAWN = CURRENTDIRECTORY.joinpath(r'assets/chess-pawn-white.png')
WHITEROOK = CURRENTDIRECTORY.joinpath(r'assets/chess-rook-white.png')

## Black Pieces
BLACKKING = CURRENTDIRECTORY.joinpath(r'assets/chess-king-black.png')
BLACKQUEEN = CURRENTDIRECTORY.joinpath(r'assets/chess-queen-black.png')
BLACKBISHOP = CURRENTDIRECTORY.joinpath(r'assets/chess-bishop-black.png')
BLACKKNIGHT = CURRENTDIRECTORY.joinpath(r'assets/chess-knight-black.png')
BLACKPAWN = CURRENTDIRECTORY.joinpath(r'assets/chess-pawn-black.png')
BLACKROOK = CURRENTDIRECTORY.joinpath(r'assets/chess-rook-black.png')