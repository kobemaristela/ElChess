WIDTH, HEIGHT = 800, 450
GRID_WIDTH, GRID_HEIGHT = 16 , 9

BLOCK_SIZE = 50   #defines the length & width of one grid square in pixels

WHITE = (255,255,255) 
BLUE = (0,0, 200)
BLACK = (0,0,0)
RED = (255,0,0)


walls = [(2,2), (3,2), (7,4), (8,4), (9,4), (4,4), (4,5), (4,6), (4,7)] #may incorporate into a Room class later, contains coordinates for non-border walls
gates = [(7,8), (8,0), (9,0), (0,5), (0,6)] #contains coordinates for any spaces where borders should not be drawn

FPS = 60