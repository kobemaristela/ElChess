WIDTH, HEIGHT = 832, 500
FPS = 60
TILE_SIZE = 64
BLACK, WHITE = (0, 0, 0), (255, 255, 255)
RED = (255, 0, 0)
GRAY = (150, 150, 150)
BROWN = (139, 105, 105)

HEALTH_BAR_WIDTH, BG_WIDTH = 100, 110
HEALTH_BAR_HEIGHT, BG_HEIGHT = 25, 35

RPG_MAP = [
['w','w','g','w','w','w','f','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','l'],
['l',' ',' ',' ',' ',' ',' ',' ','l',' ',' ',' ',' ',' ','l',' ',' ','r',' ',' ',' ',' ',' ',' ',' ',' ','l'],
['l',' ',' ',' ',' ',' ',' ',' ','l',' ',' ','l',' ',' ','l',' ',' ','r',' ',' ',' ','f',' ',' ','B',' ','l'],
['l',' ',' ',' ',' ',' ',' ',' ','l',' ',' ','l',' ',' ','l',' ',' ','r',' ',' ','g',' ',' ',' ',' ',' ','l'],
['l',' ',' ','M',' ',' ','w','w','l',' ',' ','l',' ',' ','l',' ',' ','r',' ',' ',' ',' ',' ',' ',' ',' ','l'],
['l',' ',' ',' ',' ',' ','w',' ','M',' ',' ','w','f',' ','l','M',' ','r',' ',' ',' ',' ','M',' ','p',' ','l'],
['l',' ','M',' ',' ',' ','w',' ',' ',' ',' ',' ',' ',' ','l',' ',' ','w','w','w',' ',' ',' ',' ',' ',' ','l'],
['l',' ',' ',' ',' ',' ','w',' ','g','w','w',' ',' ',' ','l',' ','r','w',' ','r',' ',' ',' ',' ',' ',' ','l'],
['w','w','d','w','f','w','w',' ',' ',' ','w',' ',' ','w','w','d','w',' ',' ','r','w',' ',' ',' ','M',' ','l'],
['l',' ',' ',' ',' ',' ','w',' ',' ',' ',' ',' ',' ',' ','l',' ',' ',' ',' ',' ','r','w',' ',' ',' ',' ','l'],
['l',' ','M',' ',' ',' ','w',' ',' ','M',' ',' ',' ','M','l',' ',' ',' ',' ',' ',' ','r','w','f','d','w','l'],
['l',' ',' ',' ',' ',' ','d',' ',' ','r',' ',' ',' ',' ','l',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','l'],
['l',' ',' ','M',' ','w','w',' ',' ','r',' ',' ',' ',' ','l',' ',' ','f','f',' ',' ',' ',' ',' ',' ',' ','l'],
['w','g','w','w','w','w','g','w','w','w','f','w','d','w','l',' ',' ',' ',' ','w',' ',' ',' ',' ','M',' ','l'],
['l',' ',' ',' ',' ',' ',' ',' ','l',' ',' ',' ',' ',' ','l',' ',' ',' ',' ',' ','f','w',' ',' ',' ',' ','l'],
['l',' ',' ',' ',' ',' ',' ',' ','l',' ',' ',' ',' ',' ','l',' ',' ',' ',' ',' ','M','w',' ',' ',' ',' ','l'],
['l',' ','w','f','w',' ','M',' ','l',' ',' ',' ',' ',' ','l',' ',' ',' ',' ',' ',' ','w',' ',' ',' ',' ','l'],
['l',' ',' ','l',' ',' ',' ',' ','l',' ','M',' ',' ',' ','l',' ',' ',' ',' ',' ',' ','w',' ',' ',' ',' ','l'],
['l',' ',' ','l',' ',' ',' ','w','l',' ',' ','w',' ',' ','w','w','w','w',' ',' ','w','w','f','w','w','w','l'],
['l',' ',' ',' ',' ',' ',' ',' ','w','d','g','w','g','w','l',' ',' ','r','d','w','l',' ',' ',' ',' ',' ','l'],
['l',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','f',' ',' ','l',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','l'],
['l',' ',' ','M',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','l',' ',' ',' ',' ',' ',' ',' ',' ','f','w',' ','l'],
['l',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','l',' ','M',' ','g','w',' ',' ',' ',' ','r',' ','l'],
['l',' ',' ',' ',' ','w',' ',' ',' ',' ','M',' ',' ',' ','l',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','l'],
['l',' ',' ',' ',' ','w',' ',' ',' ',' ',' ',' ',' ',' ','l',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','l'],
['l',' ',' ',' ',' ','w',' ',' ',' ',' ',' ',' ',' ',' ','l',' ',' ',' ',' ',' ','M',' ',' ',' ',' ',' ','l'],
['l',' ',' ','g','w','f','g',' ',' ',' ',' ',' ',' ',' ','l',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','l'],
['l',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','l',' ',' ',' ',' ',' ',' ','f',' ',' ',' ',' ','l'],
['l',' ',' ',' ',' ',' ','M',' ',' ',' ',' ',' ',' ','w','l',' ',' ',' ',' ',' ',' ','l',' ','M',' ',' ','l'],
['l',' ',' ',' ','w',' ',' ',' ',' ',' ',' ',' ','w','l','w','w','g','g','w','w','w','l',' ',' ',' ',' ','l'],
['l',' ',' ',' ',' ','w',' ',' ',' ',' ',' ',' ','w','l',' ',' ',' ',' ',' ',' ',' ','l',' ',' ',' ',' ','l'],
['l',' ',' ',' ',' ',' ','f',' ',' ',' ',' ','g','f','l',' ',' ',' ',' ','M',' ',' ','w','d','l',' ',' ','l'],
['l',' ',' ',' ','g','w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','l','M',' ','l'],
['l',' ',' ',' ',' ',' ',' ',' ','M',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','l',' ',' ','l'],
['l',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','l',' ',' ','l'],
['w','w','g','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','l']
]