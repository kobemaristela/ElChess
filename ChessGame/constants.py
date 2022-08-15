from pathlib import Path

X, Y = 560, 560

# Board Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
RED = (255, 0, 0)

board_colors = [BLUE, WHITE, RED, CYAN, MAGENTA]


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