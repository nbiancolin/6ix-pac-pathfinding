# You can modify this file to implement your own algorithm

from constants import *
import random as rnd

"""
You can use the following values from constants.py to check for the type of cell in the grid:
I = 1 -> Wall 
o = 2 -> Pellet (Small Dot)
e = 3 -> Empty
"""

global prevDir
#prevDir = -1 #if there 

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

    '''My Pac-Man logic:
    Looking at the game board this is not a typical pac man map, nor will there be ghosts running around to chase you (for now), so for now its just about finding the most efficient path.

    For now, Im going to say screw efficienct (although if I had more than ~5 hours to work on this, I'd consider it), and just find a path that works.
    So, using that old thing someone told me once in grade 3:
    "If you're in a maze, put your hand on the right wall and follow it until you get out"

    Lets see if that works lmao.

    So essentially, in code, this means that we check the surrounding cells:
        if there is only one valid move (e, o, or O), we take it
        if there are multiple valid moves, take the O or O if there is one, otherwise take the e
        there should be no invalid moves, since behind is always an option, which will be e.

    '''
    #current loc given by the tuple location

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
   
    

    if tiles.count(o) >= 1: 
        #go to that point
        prevDir = tiles.index(o)
        return moves[prevDir]
    

    if tiles[prevDir] == I:
        n = len(moves)
        for i in range(n):
            j = rnd.randint(0, n-1)
            elem = moves.pop(j)
            moves.append(elem)
            elem = tiles.pop(j)
            tiles.append(elem)

        #temp = zip(moves, tiles)
        #rnd.shuffle(temp)
        #moves, tiles = zip(*temp)
        prevDir = tiles.index(e)
        return moves[prevDir]

    return moves[prevDir]