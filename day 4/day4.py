data = open('day4input.txt','r').read().strip().split('\n')

"""
generate directions


-1 indicates go back on x-axis or y-axis (left or down)
 0 indicated stay in place x-axis or y-axis (or both, i.e. (0,0) means no movement)
 1 indicates go forward x-axis or y-axis (right or up)

"""

directions=[]
for dx in range(-1,2):
    for dy in range(-1,2):
        if dx!=0 or dy!=0:
            directions.append((dx,dy))

"""
(-1, -1), (-1, 0), (-1, 1)
( 0, -1),          ( 0, 1)
( 1, -1), ( 1, 0), ( 1, 1)

"""
numrows=len(data)
numcolumns=len(data[0])

#part 1
def hasxmas(x,y,direction):
    dx,dy=direction
    #enumerate returns both index and character i.e. (0,'X') so on
    for index, char in enumerate("XMAS"): 
        new_x= x+index*dx
        new_y=y+index*dy

        #out of bound condition
        if not (0<=new_x<numrows and 0<=new_y<numcolumns): 
            return False
        if data[new_x][new_y]!=char:
            return False
    return True

#check every direction in every cell

count=0
for rows in range(numrows):
    for columns in range(numcolumns):
        for direction in directions:
            count+=hasxmas(rows,columns,direction)

print(count)

#part 2
def xshapedmas(x,y):

    #centre may go out of range checking diagonals
    if not (0<x<numrows-1 and 0<y<numcolumns-1): 
        return False

    #if centre isn't A
    if data[x][y]!="A": 
        return False
    
    #checking diagonals
    if (f"{data[x-1][y-1]}{data[x+1][y+1]}" not in ["SM","MS"]): 
        return False
    if (f"{data[x-1][y+1]}{data[x+1][y-1]}" not in ["SM","MS"]):
        return False
    else:
        return True

countx=0   
for rows in range(numrows):
    for columns in range(numcolumns):
        countx+=xshapedmas(rows,columns)

print(countx)