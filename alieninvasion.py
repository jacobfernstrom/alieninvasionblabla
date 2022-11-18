import random
from pytimedinput import timedInput
import os   
import time

#TODO
# gränser för
#
#
#
def draw_board():
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

def points():
    for shot in active_shots: 
        if shot in active_UFO: #check if current shot is in active_ufo and remove both shot and ufo if they are
            active_shots.remove(shot)
            active_UFO.remove(shot)
            point[0] += 1 #one point given to every ufo destroyed

def ufo_shots():
    temp_var1 = random.randint(0,2)
    if temp_var1 == 0:
        if len(active_UFO) > 0:
            temp_var = random.randint(0,len(active_UFO)-1)
        
            shot_pos = active_UFO[temp_var]
            shot_pos = (shot_pos[0],shot_pos[1]+1)  
            active_UFO_shots.append(shot_pos) 

def update_ufo_shots():
    count = 0
    for shot in active_UFO_shots: 
        active_UFO_shots[count] = (shot[0], shot[1]+1) #changes height-position by -1, for every active shot
        if active_UFO_shots[count][1] == 39: #check if shot is at last position
            active_UFO_shots.pop(count) # remove shot when out of play
        count +=1 #count is to get position in list

def start_info():
    print('w = forward')
    print('a = left')
    print('d = right')
    print('space = end game')
    time.sleep(7)
    print(3)
    time.sleep(0.5)
    print(2)
    time.sleep(0.5)
    print(1)
    time.sleep(0.5)

    

height = 20
width = 41


active_shots = []
active_UFO = []
active_UFO_shots = []
point = [0]
attaxheli = [(width//2,height - 2)]

DIRECTION ={'left':(-1,0), 'right':(1,0),'up':(0,-1), 'nada':(0,0)}
direction = DIRECTION['right']

board = [(col,row) for row in range(height) for col in range(width)]
count1 = 0

playagain = 0




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
        count1 += 1
        if (width - 2, height -2) in active_UFO or (1, height - 2) in active_UFO:
            print('You lost, Aliens reached the surface of the earth')
            break
        if attaxheli[0] in active_UFO_shots:
            print('You lost, your attaxheli was destroyed')
            break
        
    




 
