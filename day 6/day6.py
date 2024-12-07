from tqdm import tqdm

#strings in python immutable,cannot be modified directly
#convert each row of the grid into a list of characters
grid = [list(line) for line in open('day6input.txt','r').read().strip().split("\n")]

rows=len(grid)
columns=len(grid[0])

#find the guard
found=False
for i in range(rows):
    for j in range(columns):
        if grid[i][j]=="^":
            found=True
            break
    if found:
        break

#for part 2
initial_i,initial_j=i,j

#part 1
direction=0

# up, right, down, left
directions=[[-1,0],[0,1],[1,0],[0,-1]]

#set of tuples, automatically handles duplicates
visited=set()

while True:
    visited.add((i,j))

    next_i=i+directions[direction][0]
    next_j=j+directions[direction][1]

    #check if guard out of bounds
    if not (0<=next_i<rows and 0<=next_j<columns):
        break

    #turn 90 degrees
    if grid[next_i][next_j]=="#":
        
        #% to keep in range 0-3
        direction=(direction+1)%4

    else:
        i,j=next_i,next_j

print(len(visited))

#part 2
def will_loop(check_i,check_j):

    #if location being checked already has an obstacle, skip it
    if grid[check_i][check_j]=="#":
        return False

    #set location as obstacle to check
    grid[check_i][check_j]="#"

    #reset starting conditions
    i,j=initial_i,initial_j
    direction=0
    new_visited=set()

    while True:

        #if current state (i, j, direction) already in new_visited
        #indicates the traversal has entered a loop
        if((i,j,direction) in new_visited):
            
            #reset grid
            grid[check_i][check_j]="."
            return True


        new_visited.add((i,j,direction))

        next_i=i+directions[direction][0]
        next_j=j+directions[direction][1]

        #if guard out of bounds then obstacle doesn't cause a loop
        if not (0<=next_i<rows and 0<=next_j<columns):

            grid[check_i][check_j]="."
            return False

        #turn 90 degrees
        if grid[next_i][next_j]=="#":
            
            #% to keep in range 0-3
            direction=(direction+1)%4

        else:
            i,j=next_i,next_j

#tqdm checks progress of loop
looplocations=0
for check_i, check_j in tqdm(visited):
    looplocations+=will_loop(check_i,check_j)

print(looplocations)   