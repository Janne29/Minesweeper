import random
from assets import window

grid = [
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
]

flag_count = 0

numbers = [1,2,3,4,5,6,7,8]

neighbors = [ [-1,-1],[0,-1],[+1,-1] , [-1,0],[+1,0] , [-1,+1],[0,+1],[+1,+1] ]


def createGrid():

    for i in range(0, 16):
        for j in range(0, 16):
            grid[i].append('')

    for i in range(0, 40):

        x = random.randint(0,15)
        y = random.randint(0,15)

        while grid[x][y] == 'bomb': 
            x = random.randint(0,15)
            y = random.randint(0,15)
        
        grid[x][y] = 'bomb'

    
def place_flag(pos):
    global flag_count

    x, y = getTile(pos[0], pos[1])

    tile = grid[x][y]

    if tile == 'flag':
        grid[x][y] = ''
        flag_count -= 1
        return

    if tile == 'flagged_bomb':
        grid[x][y] = 'bomb'
        flag_count -= 1
        return
    
    if flag_count == 40: return

    if tile == 'bomb':
        grid[x][y] = 'flagged_bomb'
        flag_count += 1
        return
    
    grid[x][y] = 'flag'
    flag_count += 1


def click_tile(pos):

    x, y = getTile(pos[0], pos[1])

    tile = grid[x][y]

    if tile in ('bomb', 'flagged_bomb'):
        grid[x][y] = 'exploded_bomb'
        return False
    
    grid[x][y] = getBombs(x,y)

    if grid[x][y] == 0: emptyTiles.clear(emptyTiles, x,y)
 
    if won(): return True





def getTile(x, y):

    for i in range(0, 16):
        if x < window.tile_size * (i + 1):
            x = i
            break
    
    for i in range(0, 16):
        if y < window.tile_size * (i + 1):
            y = i
            break
        
    return x, y

def won():

    for row in grid:
        if not (row.count('') + row.count('flag') == 0):
            return False
    return True

def getBombs(x,y):

    bombs_around = 0

    for neighbor in neighbors:

        if x == 0 and neighbor[0] == -1 or x == 15 and neighbor[0] == +1: continue
        if y == 0 and neighbor[1] == -1 or y == 15 and neighbor[1] == +1: continue

        try:

            if grid[ x + neighbor[0] ][ y + neighbor[1] ] in ('bomb', 'flagged_bomb'): bombs_around += 1
            
        except: continue

    return bombs_around

class emptyTiles:

    visited = [] 

    def clear(self, x, y):

        pos = (x,y) 
        if pos in self.visited: return
        self.visited.append(pos)

        for neighbor in neighbors:

            x += neighbor[0]
            y += neighbor[1]

            while x >= 0 and x <= 15 and y >= 0 and y <= 15:

                bombs_around = getBombs(x,y)

                if bombs_around > 0:
                    grid[x][y] = bombs_around
                    break

                grid[x][y] = 0
                self.clear(emptyTiles, x,y)
                x += neighbor[0]
                y += neighbor[1]

            x = pos[0]
            y = pos[1]
  