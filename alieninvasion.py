import random
from pytimedinput import timedInput
import os   
import time


def draw_board(): #this is borrowed from https://www.youtube.com/watch?v=lAIawk2IVIM
    for pos in board:
        
        if pos == attaxheli[0]:
            print('Y', end = '')

        elif pos[1] == 0:
            print('~', end = '')

        elif pos[1] == height - 1:
            print('x', end = '')
        
        elif pos[0] == width - 1 or pos[0] == 0:
            print('|', end = '')

        elif pos in active_shots:
            print('I', end = '') 

        elif pos in active_UFO_shots:
            print('o', end = '')

        elif pos in active_UFO:
            print('W', end ='') 

        else:
            print(' ', end = '')
        
        if pos[0] == width -1:
            print('')

def update_attaxheli(): #positional update of attaaaxheli aka 'Y'
    if direction == (-1, 0) or direction == (1, 0): #timedinput for 'a' and 'd' aka sideways movement result in these directions
        new_pos = (attaxheli[0][0]+direction[0], attaxheli[0][1]+direction[1]) #new_pos is new position of attaxheli
        if new_pos[0] == 40 or new_pos[0] == 0: #scan for borders
            new_pos = (attaxheli[0][0], attaxheli[0][1]) # if attaxheli is by border, previous location is current position

        attaxheli.insert(0, new_pos) #inserts new position in attaxheli list at position 0
        attaxheli.pop(1) #removes the previous position of attaxheli

def new_shots(): #function that create position for a new shot, by pressing 'w'
    if direction == (0, -1): #timedinput for 'w' aka shooting and result in this direction
        shot_pos = (attaxheli[0][0], attaxheli[0][1]-direction[1]) #variable that contains new shot

        active_shots.append(shot_pos) #shot is added to 'active_shots'
        
def update_shots(): #update position of all active shots
    count = 0
    for shot in active_shots: 
        active_shots[count] = (shot[0], shot[1]-1) #changes height-position by -1, for every active shot
        if active_shots[count][1] == -1: #check if shot is at last position
            active_shots.pop(count) # remove shot when out of play
        count +=1 #count is to get position in list

def create_UFO(): # randomly creates ufos
    temp_var = random.randint(0,10) # assign random number between 0 and 10 to variable
    if temp_var == 0: #if temp_var eqauls 0, one ufo is created
        active_UFO.append((1,1)) #append new ufo-position to active_UFO

def update_ufo():# update position of all UFO
    count = 0
    for ufo in active_UFO:
        if ufo[1] % 2 != 0 and ufo[0] == 39: # if ufo is on right border, ufo new position is height-1
            active_UFO[count] = (ufo[0], ufo[1] + 1)
            count+=1
        elif ufo[1] % 2 != 0 and ufo[0] != 40: #ufo go right if coming from right border
            active_UFO[count] = (ufo[0] + 1, ufo[1])
            count+=1
        elif ufo[1] % 2 == 0 and ufo[0] != 1: #ufo go right if coming from left border
            active_UFO[count] = (ufo[0] - 1, ufo[1])
            count+=1
        elif ufo[1] % 2 == 0 and ufo[0] == 1: # if ufo is on left border, ufo new position is height-1
            active_UFO[count] = (ufo[0], ufo[1] + 1)
            count+=1

def points(): #method to show if a shot and ufo is at the same position
    for shot in active_shots: 
        if shot in active_UFO: #check if current shot is in active_ufo and remove both shot and ufo if they are
            active_shots.remove(shot)
            active_UFO.remove(shot)
            point[0] += 1 #one point given to every ufo destroyed

def ufo_shots(): #create random ufo shots
    temp_var1 = random.randint(0,2) # create ufo shot app. randomly, but app. every third 1/3
    if temp_var1 == 0:
        if len(active_UFO) > 0:
            temp_var = random.randint(0,len(active_UFO)-1) #randomly select a ufo that shoot
        
            shot_pos = active_UFO[temp_var]
            shot_pos = (shot_pos[0],shot_pos[1]+1)  
            active_UFO_shots.append(shot_pos) 

def update_ufo_shots(): #update the position of the ufo shots in the grid
    count = 0
    for shot in active_UFO_shots: 
        active_UFO_shots[count] = (shot[0], shot[1]+1) #changes height-position by -1, for every active shot
        if active_UFO_shots[count][1] == 39: #check if shot is at last position
            active_UFO_shots.pop(count) # remove shot when out of play
        count +=1 #count is to get position in list

def start_info(): #starter info on how to quit, and play
    print('w = forward')
    print('a = left')
    print('d = right')
    print('space = end game')
    time.sleep(7) #didnt want timedinput, just a delay
    print(3)
    time.sleep(0.5)
    print(2)
    time.sleep(0.5)
    print(1)
    time.sleep(0.5)

    

height = 20 #grid height
width = 41 # grid width


active_shots = [] #empty lists 1
active_UFO = [] # 2
active_UFO_shots = [] # 3
point = [0] # point list, i think i can skip the zero or just go with an int variable
attaxheli = [(width//2,height - 2)] # starting position of attaxheli

DIRECTION ={'left':(-1,0), 'right':(1,0),'up':(0,-1), 'nada':(0,0)} # borrowed, https://www.youtube.com/watch?v=lAIawk2IVIM, direction which every key represents, nada =no movement, up = shooting
direction = DIRECTION['up'] 

board = [(col,row) for row in range(height) for col in range(width)]



#MAIN
start_info()


while True:
        
        os.system('clear') #cls in windows
        print('points:', point[0])
        draw_board()
        
        txt,_ = timedInput(timeout = 0.1)
        match txt:
            case 'w': direction = DIRECTION['up']
            case 'a': direction = DIRECTION['left']
            case 'd': direction = DIRECTION['right']
            case '': direction = DIRECTION['nada']
            case ' ': break
        
        update_attaxheli()
        new_shots()
        update_shots()
        create_UFO()
        update_ufo()
        ufo_shots()
        update_ufo_shots()
        points()
        if (width - 2, height -2) in active_UFO or (1, height - 2) in active_UFO: #check if ufos has reached earth, could probably make a function of this
            print('You lost, Aliens reached the surface of the earth')
            break
        if attaxheli[0] in active_UFO_shots:#checks if attaxheli and ufo-shot is at same position, could probably make a function of this
            print('You lost, your attaxheli was destroyed')
            break
        
    




 
