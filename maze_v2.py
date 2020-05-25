width = 8
height = 8
startX = 0
startY = 0
endX = 7
endY = 7
wasHere = [[0 for j in range(height) ] for i in range(width) ]
correctPath = [[0 for j in range(height) ] for i in range(width) ]

def solveMaze( maze ):
    for row in maze:
        print(row)
    #print(wasHere)
    #print(correctPath)

    if recursiveSolve( startX, startY ) == False:
        print("Solution doesn't exist")
        return False
    
    print("Solution found, Route taken to find the exit:")
    for row in correctPath:
        print(row)
    


def recursiveSolve( x, y ):
    if x == endX and y == endY:                                       #If you reached the end
        correctPath[x][y] = 1
        return True
    
    if maze[x][y]==0 or wasHere[x][y]:                                #If you are on a wall or already were here
        return False
    
    wasHere[x][y] = 1

    if x != 0:                                                         #Checks if not on left edge
        if recursiveSolve(x-1, y):                                     #Recalls method one to the left
            correctPath[x][y] = 1                                        #Sets that path value to true
            return True
    
    if x != width - 1:                                                 #Checks if not on right edge
        if recursiveSolve(x+1, y):                                         #Recalls method one to the right
            correctPath[x][y] = 1                                    #Sets that path value to true
            return True

    if y != 0:                                                         #Checls if not on top edge
        if recursiveSolve(x,y-1):                                      #Recalls method one up
            correctPath[x][y] = 1                                    #Sets that path value to true
            return True
    
    if y != height - 1:                                               #Checks if not on bottom edge
        if recursiveSolve(x,y+1):                                     #Recalls method one down
            correctPath[x][y] = 1                                    #Sets that path value to true
            return True
    return False

#Funcion principal
maze=[[1,1,1,0,1,1,1,1],[0,1,1,0,1,0,1,1],[1,0,1,0,1,0,1,1],[1,1,1,0,1,0,1,1],
[1,1,1,0,1,0,1,1],[0,1,1,0,1,0,1,1],[1,1,1,0,1,0,1,1],[1,1,1,1,1,0,1,1]]

solveMaze(maze) 