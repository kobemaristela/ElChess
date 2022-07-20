import pygame
from map_constants import *
from game_sprites import *

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Elchess Map")



#thanks to http://programarcadegames.com/index.php?chapter=introduction_to_sprites&lang=en for providing a very useful guide on sprites

def load_wall(walls, wall_group: pygame.sprite.Group, all_sprites: pygame.sprite.Group):
    for wall in walls:
        wall_sprite = WallSprite(BLACK, BLOCK_SIZE, BLOCK_SIZE, wall)
        wall_group.add(wall_sprite)
        all_sprites.add(wall_sprite)
def load_standard_borders(gate_coordinates, wall_sprites: pygame.sprite.Group, all_sprites: pygame.sprite.Group):
    for i in range(max(GRID_HEIGHT, GRID_WIDTH)):
        border_coordinate = (0,i)
        #left border
        if border_coordinate not in gate_coordinates and i < GRID_HEIGHT:
            wall_sprite = WallSprite(BLACK, BLOCK_SIZE, BLOCK_SIZE, border_coordinate)
            wall_sprites.add(wall_sprite)
            all_sprites.add(wall_sprite)
        #right border
        border_coordinate = (GRID_WIDTH - 1, i)
        if border_coordinate not in gate_coordinates and i < GRID_HEIGHT:
            wall_sprite = WallSprite(BLACK, BLOCK_SIZE, BLOCK_SIZE, border_coordinate)
            wall_sprites.add(wall_sprite)
            all_sprites.add(wall_sprite)
        #bottom border
        border_coordinate = (i, GRID_HEIGHT - 1)
        if border_coordinate not in gate_coordinates and i < GRID_WIDTH:
            wall_sprite = WallSprite(BLACK, BLOCK_SIZE, BLOCK_SIZE, border_coordinate)
            wall_sprites.add(wall_sprite)
            all_sprites.add(wall_sprite)
        #top border
        border_coordinate = (i, 0)
        if border_coordinate not in gate_coordinates and i < GRID_WIDTH:
            wall_sprite = WallSprite(BLACK, BLOCK_SIZE, BLOCK_SIZE, border_coordinate)
            wall_sprites.add(wall_sprite)
            all_sprites.add(wall_sprite)
        

def handle_hero_movement(key_event: pygame.event.Event, hero_sprite: HeroSprite, wall_sprites: pygame.sprite.Group):
    if key_event.key == pygame.K_w and hero_sprite.rect.y - BLOCK_SIZE > 0:
        hero_sprite.rect.y -= BLOCK_SIZE
        if pygame.sprite.spritecollide(hero_sprite, wall_sprites, False): #does it cause a collision?
            hero_sprite.rect.y += BLOCK_SIZE #if so, disallow movement to that direction
    if key_event.key == pygame.K_s and hero_sprite.rect.y + BLOCK_SIZE < HEIGHT:
        hero_sprite.rect.y += BLOCK_SIZE
        if pygame.sprite.spritecollide(hero_sprite, wall_sprites, False):
            hero_sprite.rect.y -= BLOCK_SIZE
    if key_event.key == pygame.K_a and hero_sprite.rect.x - BLOCK_SIZE > 0:
        hero_sprite.rect.x -= BLOCK_SIZE
        if pygame.sprite.spritecollide(hero_sprite, wall_sprites, False):
            hero_sprite.rect.x += BLOCK_SIZE
    if key_event.key == pygame.K_d and hero_sprite.rect.x + BLOCK_SIZE + hero_sprite.rect.width < WIDTH:
        hero_sprite.rect.x += BLOCK_SIZE
        if pygame.sprite.spritecollide(hero_sprite, wall_sprites, False):
            hero_sprite.rect.x -= BLOCK_SIZE


def draw_window(all_sprites_list: pygame.sprite.Group):
    WIN.fill(WHITE)
    draw_grid()
    all_sprites_list.draw(WIN)
    pygame.display.update()


# thanks to https://stackoverflow.com/a/61007670
def draw_grid():
    block_size = BLOCK_SIZE #Set the size of the grid block
    for x in range(0, WIDTH, block_size):
        for y in range(0, HEIGHT, block_size):
            rect = pygame.Rect(x, y, block_size, block_size)
            pygame.draw.rect(WIN, BLACK, rect, 1)


def main():

    hero_rect = pygame.Rect(WIDTH //2 - 3 * BLOCK_SIZE // 4, HEIGHT - 3 * BLOCK_SIZE // 4, BLOCK_SIZE // 2, BLOCK_SIZE // 2)

    hero_sprite = HeroSprite(BLUE, BLOCK_SIZE // 2, BLOCK_SIZE // 2, (hero_rect.x, hero_rect.y))
    wall_sprites = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(hero_sprite)

    clock = pygame.time.Clock()
    run = True

    load_wall(walls, wall_sprites, all_sprites)
    load_standard_borders(gates,wall_sprites, all_sprites)

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYUP:
                handle_hero_movement(event, hero_sprite, wall_sprites)
        draw_window(all_sprites)
    pygame.quit()

if __name__ == "__main__":
    main()