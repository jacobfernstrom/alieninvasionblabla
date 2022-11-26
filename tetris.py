from random import randint
import os
from pytimedinput import timedInput




#gameplay_function

def draw_board ():
    for pos in game_board:
        if pos[1] == 0 or pos[1] == grid_width-1:
            print('!', end = '')

        elif pos[0] == grid_height - 1:
            print('^', end = '')
        
        elif pos in new_block:
            print('#', end = '')
        
        elif pos in bottom_blocks:
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
                new_block.append((start_pos_block[0],start_pos_block[1] + i))
                new_block.append((start_pos_block[0]+1,start_pos_block[1] + i))    
                
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


     
    
    print

def update_tetroid ():
    count = 0
    count_two = 0
    
    for part in new_block:
        if part[1] == grid_width - 2:
            count +=1
        elif part[1]== 1:
            count_two += 1
    
    
    for i in range(len(new_block)):
        if count > 0 and direction == (0, -1):
            new_block[i] = (new_block[i][0]+direction[0], new_block[i][1] + direction[1])
        elif count_two > 0 and direction == (0, 1):
            new_block[i] = (new_block[i][0]+direction[0], new_block[i][1] + direction[1])
        elif count == 0 and count_two == 0:
            new_block[i] = (new_block[i][0]+direction[0], new_block[i][1] + direction[1])
        
        
   
        

    
            

    for i in range(len(new_block)): # pushe tetroid down one step
        new_block[i] = (new_block[i][0]+1, new_block[i][1])

def check_bottom():
    global count_bottom
    count_bottom = 0
    for part in new_block:
        part_temp = (part[0] + 1, part[1])
        if (part_temp in bottom_blocks) or part_temp[0] == grid_height-1:
            count_bottom =1
    if count_bottom == 1:
        bottom_blocks.extend(new_block)
        new_block.clear()
    

#functions/methods






#declarables 
grid_height = 18
grid_width = 12

#LISTS
start_pos_block = (0,grid_width/2)
new_block = []
bottom_blocks = []

#directional data
DIRECTION ={'left':(0,-1), 'right':(0,1),'up':(0,0), 'end_game':(0,0), 'down':(1,0)} 
direction = DIRECTION['up'] 

#col/row loop
game_board = [(col,row) for col in range(grid_height) for row in range(grid_width)]



#MAIN_loop
while True:
    draw_tetroid()
    
    draw_board()
    txt,_ = timedInput(timeout = 0.5)
    match txt:
        case 'w': direction = DIRECTION['up']
        case 'a': direction = DIRECTION['left']
        case 'd': direction = DIRECTION['right']
        case '': direction = DIRECTION['end_game']
        case ' ': break
    update_tetroid()
    check_bottom()
    