import pygame
from Realms.map_constants import *
from game_sprites import *
from Realms.room import Room
from Mobs.monster import Monster
from Mobs.hero import Hero
from pygame_main import Button

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Elchess Map")



#thanks to http://programarcadegames.com/index.php?chapter=introduction_to_sprites&lang=en for providing a very useful guide on sprites

def load_wall(walls, wall_group: pygame.sprite.Group):
    for wall in walls:
        wall_sprite = WallSprite(BLACK, BLOCK_SIZE, BLOCK_SIZE, wall)
        wall_group.add(wall_sprite)
def load_standard_borders(gate_coordinates, wall_sprites: pygame.sprite.Group):
    for i in range(max(GRID_HEIGHT, GRID_WIDTH)):
        border_coordinate = (0,i)
        #left border
        if border_coordinate not in gate_coordinates and i < GRID_HEIGHT:
            wall_sprite = WallSprite(BLACK, BLOCK_SIZE, BLOCK_SIZE, border_coordinate)
            wall_sprites.add(wall_sprite)
        #right border
        border_coordinate = (GRID_WIDTH - 1, i)
        if border_coordinate not in gate_coordinates and i < GRID_HEIGHT:
            wall_sprite = WallSprite(BLACK, BLOCK_SIZE, BLOCK_SIZE, border_coordinate)
            wall_sprites.add(wall_sprite)
        #bottom border
        border_coordinate = (i, GRID_HEIGHT - 1)
        if border_coordinate not in gate_coordinates and i < GRID_WIDTH:
            wall_sprite = WallSprite(BLACK, BLOCK_SIZE, BLOCK_SIZE, border_coordinate)
            wall_sprites.add(wall_sprite)
        #top border
        border_coordinate = (i, 0)
        if border_coordinate not in gate_coordinates and i < GRID_WIDTH:
            wall_sprite = WallSprite(BLACK, BLOCK_SIZE, BLOCK_SIZE, border_coordinate)
            wall_sprites.add(wall_sprite)

        

def handle_hero_movement(key_event: pygame.event.Event, hero_sprite: Hero, wall_sprites: pygame.sprite.Group):
    if key_event.key == pygame.K_w:
        hero_sprite.rect.y -= BLOCK_SIZE
        if pygame.sprite.spritecollide(hero_sprite, wall_sprites, False): #does it cause a collision?
            hero_sprite.rect.y += BLOCK_SIZE #if so, disallow movement to that direction
    if key_event.key == pygame.K_s:
        hero_sprite.rect.y += BLOCK_SIZE
        if pygame.sprite.spritecollide(hero_sprite, wall_sprites, False):
            hero_sprite.rect.y -= BLOCK_SIZE
    if key_event.key == pygame.K_a:
        hero_sprite.rect.x -= BLOCK_SIZE
        if pygame.sprite.spritecollide(hero_sprite, wall_sprites, False):
            hero_sprite.rect.x += BLOCK_SIZE
    if key_event.key == pygame.K_d:
        hero_sprite.rect.x += BLOCK_SIZE
        if pygame.sprite.spritecollide(hero_sprite, wall_sprites, False):
            hero_sprite.rect.x -= BLOCK_SIZE


def handle_room_change(hero_sprite: Hero, current_room: Room, wall_sprites: pygame.sprite.Group):
    next_room = current_room

    if hero_sprite.rect.y < 0 and current_room.top_room:
        hero_sprite.rect.y += GRID_HEIGHT * BLOCK_SIZE #move hero to bottom of screen
        next_room = current_room.top_room
    if hero_sprite.rect.y  > HEIGHT and current_room.bottom_room:
        hero_sprite.rect.y -= GRID_HEIGHT * BLOCK_SIZE
        next_room = current_room.bottom_room
    if hero_sprite.rect.x  < 0 and current_room.left_room:
        hero_sprite.rect.x += GRID_WIDTH * BLOCK_SIZE
        next_room = current_room.left_room
    if hero_sprite.rect.x  > WIDTH  and current_room.right_room:
        hero_sprite.rect.x -= GRID_WIDTH * BLOCK_SIZE
        next_room = current_room.right_room
    if not next_room  == current_room:
        wall_sprites.empty()
        load_standard_borders(next_room.gates, wall_sprites)
        load_wall(next_room.walls, wall_sprites)
        return next_room
    return current_room

def draw_window(*sprite_groups: pygame.sprite.Group):
    WIN.fill(WHITE)
    draw_grid()
    for group in sprite_groups:
        group.draw(WIN)
        



# thanks to https://stackoverflow.com/a/61007670
def draw_grid():
    block_size = BLOCK_SIZE #Set the size of the grid block
    for x in range(0, WIDTH, block_size):
        for y in range(0, HEIGHT, block_size):
            rect = pygame.Rect(x, y, block_size, block_size)
            pygame.draw.rect(WIN, BLACK, rect, 1)


def main():

    mode = "map"

    left_room = Room([],[(GRID_WIDTH -1, 6),(GRID_WIDTH - 1, 5)],[0,0,0,0])
    top_room = Room([(5,5),(5,6),(6,6),(6,5)],[(8,GRID_HEIGHT -1), (9, GRID_HEIGHT - 1)],[0,0,0,0])
    beginning_room = Room(walls, gates, [left_room,0,top_room,0])

    #these lines are suboptimal, need to restructure Room class to improve scalability
    top_room.bottom_room = beginning_room
    left_room.right_room = beginning_room

    current_room = beginning_room

    hero_initial_pos = pygame.Rect(WIDTH //2 - 3 * BLOCK_SIZE // 4, HEIGHT - 3 * BLOCK_SIZE // 4, BLOCK_SIZE // 2, BLOCK_SIZE // 2)

    hero_sprite_group = pygame.sprite.Group()
    hero = Hero("Bill")
    hero.rect.x = hero_initial_pos.x
    hero.rect.y = hero_initial_pos.y
    hero_sprite_group.add(hero)


    wall_sprites = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(hero)

    monsters = pygame.sprite.Group()
    monster1 = Monster(175, 175)
    monster2 = Monster(275,225)
    monsters.add(monster1,monster2)

    #from Timothy's pygame_main file
    attack_button_img = pygame.image.load('attack_button.png').convert_alpha()
    flee_button_img = pygame.image.load('flee_button.png').convert_alpha()
    player_attack_button = Button(50, 300, attack_button_img, 0.65) #changed y coordinate
    player_flee_button = Button(450, 300, flee_button_img, 0.65)

    clock = pygame.time.Clock()
    run = True

    load_wall(current_room.walls, wall_sprites)
    load_standard_borders(current_room.gates,wall_sprites)

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYUP and mode == "map":
                handle_hero_movement(event, hero, wall_sprites)
        
        current_room = handle_room_change(hero, current_room, wall_sprites)
        draw_window(wall_sprites, monsters, hero_sprite_group)


        #from Timothy's pygame_main.py
        monster_to_attack = pygame.sprite.spritecollideany(hero, monsters, pygame.sprite.collide_rect_ratio(3)) #last arg allows for collisions in tiles around the monster
        if monster_to_attack:
            mode = "battle" #disallow player movement while in battle
            print(monster_to_attack)
            if player_attack_button.draw(WIN):
                print(monster_to_attack)
                hero.attack(monster_to_attack)
                print(monster_to_attack)

                if monster_to_attack.hp <= 0:
                    monster_to_attack.kill()
                    mode = "map"
            
            player_flee_button.draw(WIN)
        pygame.display.update() #should preferably be in draw_window(), must find way to incorporoate button pop-up into said function.
        
    pygame.quit()

if __name__ == "__main__":
    main()