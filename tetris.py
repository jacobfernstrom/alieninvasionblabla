from random import randint
import os
from pytimedinput import timedInput
#TODO
# 1. rita upp en spelplan
# 2. definiera block, 5 funktioner? block, rad, zickzack, kant, alla block har 4x#
# 3. listor, aktivt block, kommande_block, block som nått botten,
# 4. 
#
#




#gameplay_function

def draw_board ():
    for pos in game_board:
        if pos[1] == 0 or pos[1] == grid_width-1:
            print('!', end = '')

        elif pos[0] == grid_height - 1:
            print('^', end = '')
        
        elif pos in new_block:
            print('#', end = '')
       
        else:
            print(' ', end = '')
        
        
        
        if pos[1] == grid_width-1:
            print('')

def draw_tetroid (): # assign start position to tetroid
    if len(new_block) == 0:   
        temp_var = randint(0,6)
        

        if temp_var == 0: #start position of O-block
            for i in range(2):
                new_block.append((start_pos_block[0]+1,start_pos_block[1] + i))
                new_block.append((start_pos_block[0],start_pos_block[1] + i))
                
        elif temp_var == 1: # starting position of I-block
            for i in range(4):
                new_block.append((start_pos_block[0] + i,start_pos_block[1]))

        elif temp_var == 2: # starting position of L-block
            for i in range(3):
                new_block.append((start_pos_block[0],start_pos_block[1] + i))
            new_block.append((start_pos_block[0] + 1,start_pos_block[1]))

        elif temp_var == 3: # starting position of T-block
            new_block.append((start_pos_block[0],start_pos_block[1]))
            for i in range(3):
                new_block.append((start_pos_block[0] + 1,start_pos_block[1] + (i - 1)))

        elif temp_var == 4: # starting position of S-block
            for i in range(2):
                new_block.append((start_pos_block[0],start_pos_block[1] + i))
                new_block.append((start_pos_block[0] + 1,start_pos_block[1] - i))

        elif temp_var == 5: # starting position of S-block
            for i in range(2):
                new_block.append((start_pos_block[0],start_pos_block[1] - i))
                new_block.append((start_pos_block[0] + 1,start_pos_block[1] + i))

        elif temp_var == 6: # starting position of L-block
            for i in range(3):
                new_block.append((start_pos_block[0],start_pos_block[1] + i))
        
            new_block.append((start_pos_block[0] + 1,start_pos_block[1] + 2))

        

def update_movement ():
    active_block = new_block
    print

def update_tetroid ():
    for i in range(len(new_block)):
        new_block[i] = (new_block[i][0] + direction[0], new_block[i][1] + direction[1])
    for i in range(len(new_block)):
        new_block[i] = (new_block[i][0]+1, new_block[i][1])
    
def check_bottom():
    print


#functions/methods






#declarables

grid_height = 18
grid_width = 12
start_pos_block = (0,grid_width/2-1)
new_block = []
active_block = []
end_block = []

DIRECTION ={'left':(0,-1), 'right':(0,1),'up':(0,0), 'end_game':(0,0), 'down':(1,0)} 
direction = DIRECTION['up'] 

game_board = [(col,row) for col in range(grid_height) for row in range(grid_width)]



#MAIN_loop
while True:
    draw_tetroid()
    print(new_block)
    draw_board()
    txt,_ = timedInput(timeout = 0.7)
    match txt:
        case 'w': direction = DIRECTION['up']
        case 'a': direction = DIRECTION['left']
        case 'd': direction = DIRECTION['right']
        case '': direction = DIRECTION['end_game']
        case ' ': break
    update_tetroid()
    