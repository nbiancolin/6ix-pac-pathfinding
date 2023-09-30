# You can modify this file to implement your own algorithm

from constants import *
import random as rnd

"""
You can use the following values from constants.py to check for the type of cell in the grid:
I = 1 -> Wall 
o = 2 -> Pellet (Small Dot)
e = 3 -> Empty
"""

global prevDir #short for Previous Direction, 
prevDir = -1

def get_next_coordinate(grid, location):
    global prevDir

    """
    Calculate the next coordinate for 6ix-pac to move to.
    Check if the next coordinate is a valid move.

    Parameters:
    - grid (list of lists): A 2D array representing the game board.
    - location (list): The current location of the 6ix-pac in the form (x, y).

    Returns:
    - list or tuple: 
        - If the next coordinate is valid, return the next coordinate in the form (x, y) or [x,y].
        - If the next coordinate is invalid, return None.
    """

   
    #IT WORKS IT JUST TAKES A WHILE
    # When I ran it, it finished in ~600 seconds 
    # please let me on your team I would very much like to be a part of it, 
    # I cannot figure out for the life of me why it keeps bouncing sometimes

    curPos = location #its not personal, I think location is too vague and don't like typing it out

    moves = [[curPos[0], curPos[1]+1],  #up (0)
             [curPos[0], curPos[1]-1],  #down (1)
             [curPos[0]+1, curPos[1]],  #right (2)
             [curPos[0]-1, curPos[1]]]  #left (3)
    
    'Removing this bc it caused a lot of back and forth stuff'
    #moves = sorted(oldMoves, key = lambda x: rnd.random()) #randomizes (hopefully) the list of moves, that way

    tiles = [] #gets values at move
    for elem in moves:
        tiles.append(grid[elem[0]][elem[1]]) #maybe make lambda function? idk if thats faster I just know its a thing
    
    #apply logic
   
    if tiles[prevDir] == o: #if the pacbot continues in its current direction, it will eat a pellet
        return moves[prevDir]  


    if tiles.count(o) >= 1: #if there are more than one pellet, pick one based on the order above (could be random but idc)
        #go to that point
        prevDir = tiles.index(o)
        return moves[prevDir]
    

    if tiles[prevDir] != I: #if there is no wall in the same direction, continue in prev direction
        return moves[prevDir]  
 
    if tiles[prevDir] == I:     #if in its current direction
                                #DO NOT USE INVERSE OF prevDir (then it gets stuck in an infinte loop)
        if (prevDir + 1) % 2 == 0: #removes the inverse so the pacbot doesnt get stuck going back and forth (like it was when writing this)
            #moves.pop(prevDir -1)
            tiles[prevDir-1] = 69

        else:
            #moves.pop(prevDir +1)
            tiles[prevDir+1] = 69 

        for i in range(3):
            if tiles[i] == I:
                #moves[i] = 69
                tiles[i] = 69

        print("========") #I hate when code doesn't work
        print(tiles)
        print(moves)
        print("========")

        #if there's only one open space, go there
        if tiles.count(e) == 1: 
            prevDir = tiles.index(e)
            return moves[prevDir]
        #shuffle list so it doesnt get stuck in an infinite loop
        
        n = 3 #length of array will always be 4 (try 3? idk)
        for i in range(n):
            j = rnd.randint(0, n-1)
            elem = moves.pop(j)
            moves.append(elem)
            elem = tiles.pop(j)
            tiles.append(elem)
        prevDir = tiles.index(e)
        return moves[prevDir]
    #return moves[prevDir]


    #advanced engineering mathematics is the most fun course of 2nd year ece change my mind :p (pls push this) 
