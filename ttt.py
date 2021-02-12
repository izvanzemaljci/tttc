import sys
import pygame

def on_click():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    mousepos_to_grid(mouse_x,mouse_y)
    display_score()
    display_player_turn()

def set_player():
    global player
    if(player == 1):
        player += 1
    elif(player == 2):
        player = 1

def mousepos_to_grid(mouse_x,mouse_y):
    if(mouse_x < 100 and mouse_y < 100):
        assign_grid_value(0,0)
    if(mouse_x < 100 and mouse_y > 100 and mouse_y < 200):
        assign_grid_value(0,1)
    if(mouse_x < 100 and mouse_y > 200 and mouse_y < 300):
        assign_grid_value(0,2)
    if(mouse_x > 100 and mouse_x < 200 and mouse_y < 100):
        assign_grid_value(1,0)
    if(mouse_x > 100 and mouse_x < 200 and mouse_y > 100 and  mouse_y < 200):
        assign_grid_value(1,1)
    if(mouse_x > 100 and mouse_x < 200 and  mouse_y > 200 and mouse_y < 300):
        assign_grid_value(1,2)
    if(mouse_x > 200 and mouse_x < 300 and mouse_y < 100):
        assign_grid_value(2,0)
    if(mouse_x > 200 and mouse_x < 300 and mouse_y > 100 and mouse_y < 200):
        assign_grid_value(2,1)
    if(mouse_x > 200 and mouse_x < 300 and mouse_y > 200 and mouse_y < 300):
        assign_grid_value(2,2)

def assign_grid_value(x,y):
    if(grid[x][y] > 0):
        return
    else:
        grid[x][y] = player
        update_grid_graphics(x,y)
        set_player()

def update_grid_graphics(x_pos,y_pos):
    if(player == 1): 
        draw_x(x_pos * cell_size,y_pos * cell_size)
    elif(player == 2):
        draw_o(x_pos * cell_size,y_pos * cell_size)

def get_mouse_position():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    return mouse_x, mouse_y

def draw_background_grid():
    x_color = (0,0,0)
    o_color = (15,56,15)
    for row in range(cell_number):
            if row % 2 == 0:
                for col in range(cell_number):
                    if col % 2 == 0:
                        grid_rect = pygame.Rect(col * cell_size,row * cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen,x_color,grid_rect)
                    else:
                        grid_rect = pygame.Rect(col * cell_size,row * cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen,o_color,grid_rect)
            else:
                for col in range(cell_number):
                    if col % 2 != 0:
                        grid_rect = pygame.Rect(col * cell_size,row * cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen,x_color,grid_rect)
                    else:
                        grid_rect = pygame.Rect(col * cell_size,row * cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen,o_color,grid_rect)

def draw_x(x_pos,y_pos):
    x_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
    x = pygame.image.load('x.png').convert_alpha()
    screen.blit(x, x_rect)

def draw_o(x_pos,y_pos):
    o_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
    o = pygame.image.load('o.png').convert_alpha()
    screen.blit(o, o_rect)

def is_game_over():
    if(grid[0][0] == grid[0][1] == grid[0][2] == player):
        return True
    if(grid[1][0] == grid[1][1] == grid[1][2] == player):
        return True
    if(grid[2][0] == grid[2][1] == grid[2][2] == player):
        return True
    if(grid[0][0] == grid[1][0] == grid[2][0] == player):
        return True
    if(grid[0][1] == grid[1][1] == grid[2][1] == player):
        return True
    if(grid[0][2] == grid[1][2] == grid[2][2] == player):
        return True
    if(grid[0][0] == grid[1][1] == grid[2][2] == player):
        return True
    if(grid[0][2] == grid[1][1] == grid[2][0] == player):
        return True

def display_player_turn():
    score_surface = game_font.render((chr(60) + "player " + str(player) + " turn" + chr(60)),True,(155,188,15),True)
    score_rect = score_surface.get_rect(center=(150,305))
    screen.blit(score_surface,score_rect)

def display_score():
    if is_game_over():
        print("Player " + str(player) + " won")

pygame.init()
cell_size = 100
cell_number = 3
screen = pygame.display.set_mode((cell_size * cell_number,cell_size * cell_number + 20))
clock = pygame.time.Clock()
game_font = pygame.font.Font('EarlyGameBoy.ttf', 15)

player = 1 #1 for x, 2 for o 
grid = [[0]*cell_number for _ in range(cell_number)]

draw_background_grid()
display_player_turn()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            on_click()
    
    pygame.display.update()
    clock.tick(60)