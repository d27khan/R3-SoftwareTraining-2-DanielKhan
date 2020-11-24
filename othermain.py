import pygame
import random
import math


WIDTH = 800
HEIGHT = 800
FPS = 30
MARGIN = 50

gridSize = 8 #input("Enter size, n (note it will be size n x n): ")
grid = []
visited = []

cellSize = WIDTH/gridSize ## 100 pixels
cellSize = math.floor(cellSize)


class cell():
    def __init__(self,r,c):
        self.r = r
        self.c = c
        N= True
        S= True
        E= True
        W= True

        self.walls = [N,S,E,W] 
        self.neigh = []
        self.numofneigh = 0


    #---- Draws Indiviual Cell ----
    def drawCell(self):
        r = self.r
        c= self.c
        x=1
        if (self.walls[0]): #North
            pygame.draw.lines(screen, green, False, [(r * cellSize, c * cellSize),((r + x) * cellSize, c * cellSize)],3)
        if (self.walls[1]): #south
            pygame.draw.lines(screen, blue, False, [(r * cellSize, (c + x )*cellSize),((r + 1) * cellSize,(c + x) * cellSize)],6) 
        if (self.walls[2]): #east
            pygame.draw.lines(screen, black, False, [((r + x) * cellSize , c * cellSize),((r + x) * cellSize ,(c + x) * cellSize)],10)
        if (self.walls[3]): #West
            pygame.draw.lines(screen, red, False, [(r * cellSize , c * cellSize),(r * cellSize ,(c + x) * cellSize)],3)
            


    #---- Removes a single wall ----
    def remove(self,w):
        self.walls[w]= False
        


    #---- Checks the Neighbor cells ----
    def checkNeighbor(self):
        r = self.r
        c = self.c
        x=1
        if (c > 0): #north
            if(grid[r][c-x] not in visited):         
                self.neigh.append(grid[r][c-x])
                self.numofneigh+=1   
        if (c < gridSize-x): #south
            if(not(grid[r][c+x] in visited)):
                self.neigh.append(grid[r][c+x])
                self.numofneigh+=1
        if (r < gridSize-x): #east
            if(grid[r+x][c] not in visited):
                self.neigh.append(grid[r+x][c])
                self.numofneigh+=1
        if (r > 0):           #west
            if(grid[r-x][c] not in visited):
                self.neigh.append(grid[r-x][c])
                self.numofneigh+=1
        

        
        #If in visited, do not store in neighbour, else add in neighbour
 

#---- Removes current wall and coresponding neighbor cell wall ---- 
def removeWalls(curr,next):
    if( curr.r == next.r and curr.c > next.c): #north
        curr.walls[0]= False
        next.walls[1]= False
    if( curr.r == next.r and curr.c < next.c): #south
        curr.walls[1]= False
        next.walls[0]= False
    if( curr.r <next.r and curr.c == next.c): #east
        curr.walls[2]= False
        next.walls[3]= False
    if( curr.r > next.r and curr.c == next.c): #west
        curr.walls[3]= False
        next.walls[2]= False
    



#---- removes neighbor cell from neigh ----
def removeNeigh(cur,nex):
        #cur.numofneigh-=1
        cur.neigh.remove(nex)

#----Makes Cell grid----
for row in range(gridSize):
    grid.append([])
    for col in range(gridSize):
        h = cell(row, col)
        grid[row].append(h)     


#----Draws completed maze----
def drawMaze():
    for row in range(gridSize):
        for col in range(gridSize):
            grid[row][col].drawCell()



#initialize pygame

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("grid")
clock = pygame.time.Clock()
white = [255,255,255]
black = [0,0,0]
green = [0,255,0]
red = [255,0,0]
blue = [0,0,255]
screen.fill(white)

startingCell = grid[random.randint(0,gridSize-1)][random.randint(0,gridSize-1)]
startingCell.checkNeighbor()

visited.append(startingCell)

randneigh = startingCell.neigh[random.randint(0,startingCell.numofneigh-1)]

removeWalls(startingCell,randneigh)

visited.append(randneigh)

#--- now loop from this point ---
while ( len(visited) != int(math.pow(len(grid),2))):

    g = len(visited)
    currentCell = visited[random.randint(0,g-1)]
    currentCell.checkNeighbor()
    neighCell = currentCell.neigh[random.randint(0,currentCell.numofneigh-1)]

    removeWalls(currentCell, neighCell)
    
    
    #removeNeigh(currentCell,neighCell)
    
    visited.append(neighCell)

drawMaze()


pygame.display.update()
running = True

while running:
    #keep running at the the right speed
    clock.tick(FPS)
    #process input (events)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False




