#!/usr/bin/env python
# coding: utf-8

# In[1]:


from __future__ import print_function
import sys
moves = []

for x in range (0, 9) :
    moves.append(str(x + 1))

P1turn = True
result = False


# Board for the game

def Game() :
    print( '\n -----')
    print( '|' + moves[0] + '|' + moves[1] + '|' + moves[2] + '|')
    print( ' -----')
    print( '|' + moves[3] + '|' + moves[4] + '|' + moves[5] + '|')
    print( ' -----')
    print( '|' + moves[6] + '|' + moves[7] + '|' + moves[8] + '|')
    print( ' -----\n')
    
count=0

f=0  

while not result :

    Game()
    
# If draw , end loop

    if(count>=9):
        print("Draw\n")
        f=1
        break
        
    if P1turn :
        print( "Player 1:")
    else :
        print( "Player 2:")

    try:
        move = int(input(">> "))
    except:
        print("Enter a valid field")
        continue
        
    if(move>9):
        print("Enter a valid move")
        continue
        
    if moves[move - 1] == 'X' or moves [move-1] == 'O':
        print("Illegal move, Try again")
        continue

    if P1turn :
        count+=1
        moves[move - 1] = 'X'
    else :
        count+=1
        moves[move - 1] = 'O'

        
    P1turn = not P1turn
    
# Considering all possible moves for someone to win

    for x in range (0, 3) :
        y = x * 3
        if (moves[y] == moves[(y + 1)] and moves[y] == moves[(y + 2)]) :
            result = True
            Game()
        if (moves[x] == moves[(x + 3)] and moves[x] == moves[(x + 6)]) :
            result = True
            Game()

            
    if((moves[0] == moves[4] and moves[0] == moves[8]) or 
       (moves[2] == moves[4] and moves[4] == moves[6])) :
        result = True
        Game()

# If not draw, print player who wins     

if (f==0):        
    print ("Player " + str(int(P1turn + 1)) + " wins\n")
    
    


# In[ ]:




