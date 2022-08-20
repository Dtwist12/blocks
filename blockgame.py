from tkinter import BROWSE
import pygame
import sys
import random


pygame.init()

# set display

WIDTH = 900
HEIGHT = 700
BACKGROUND = (0,0,0)
PINK = (255,0,255)
CYAN = (0,255,255)
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)

#player
player_size = 50
player_position = [WIDTH /2, HEIGHT-2*player_size]

#opponent
opponent_size = 50
opponent_position = [random.randint(0,WIDTH-opponent_size),0]
opponent_list =[opponent_position]
SPEED = 10



#timing
game_over = False
clock = pygame.time.Clock()

def drop_opponent(opponent_list):
    if len(opponent_list) < 10:
        x_pos = random.randint(0, WIDTH-opponent_size)
        y_pos = 0
        opponent_list.append([x_pos,y_pos])
################################################################
def draw_opponent(opponent_list):
    for opponent_position in opponent_list:
        pygame.draw.rect(screen, CYAN, (opponent_position[0], opponent_position[1], opponent_size,opponent_size))

def update_opponent_position(opponent_list):
    for idx, opponent_position in enumerate (opponent_list):
        if opponent_position[1] >= 0 and opponent_position[1] < HEIGHT:
           opponent_position[1] += SPEED
        else:
            opponent_list.pop(idx)

def collision_check(opponent_list, player_position):
    for opponent_position in opponent_list:
        if detect_collision(opponent_position , player_position):
            return True
    return False



def detect_collision(player_position, opponent_position):
    p_x = player_position[0]
    p_y = player_position[1]

    o_x = opponent_position[0]
    o_y = opponent_position[1]
    
    if (o_x >= p_x and o_x < (p_x + player_size)) or (p_x >= o_x and p_x < (o_x + opponent_size)):
        if (o_y >= p_y and o_y < (p_y + player_size)) or (p_y >= o_y and p_y < (o_y + opponent_size)):
            return True
    return False


while not game_over:

    for event in pygame.event.get():
      
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:

            x = player_position[0]
            y = player_position[1]

            if event.key == pygame.K_LEFT:
                x -= player_size
            elif event.key == pygame.K_RIGHT:
                x += player_size
            elif event.key == pygame.K_UP:
                y -= player_size
            elif event.key == pygame.K_DOWN:
                y += player_size 
            player_position = [x, y]





    #fill screen
    screen.fill(BACKGROUND)

    #falling block loop
    # if opponent_position[1] >= 0 and opponent_position[1] < HEIGHT:
    #     opponent_position[1] += SPEED
    # else:
    #     opponent_position[0] = random.randint(0, WIDTH-opponent_size)
    #     opponent_position[1] = 0

    # if detect_collision(player_position, opponent_position):
    #     game_over = True
        

    drop_opponent(opponent_list)
    update_opponent_position(opponent_list)

    if collision_check(opponent_list, player_position):
        game_over = True
        break
    draw_opponent(opponent_list)

    pygame.draw.rect(screen, PINK, (player_position[0], player_position[1], player_size, player_size))
    

    clock.tick(30) 
    pygame.display.update()

# #score board
# score = 0

# # falling blocks
# rain_size = 50
# rain_list = []

# speed = 10
# amount = 50




