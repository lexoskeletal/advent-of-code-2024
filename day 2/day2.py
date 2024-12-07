data=open('day2input.txt','r').read().split('\n')

safe_sequences=0
dampened_safe_sequence=0

def checksafe(sequence):

    #to check if sequence is increasing or decreasing
    increasing=False
    decreasing=False

    for i in range(len(sequence)-1):
        level_difference=sequence[i+1]-sequence[i]
        if level_difference>0:
            increasing=True
        if level_difference<0:
            decreasing=True
            
        #if both, sequence is unsafe
        if increasing==True and decreasing==True: 
            return False
        if abs(level_difference)>3 or abs(level_difference)<1:
            return False
    return True

def dampener(sequence):
    for i in range(len(sequence)):

        #delete an element, make copy
        dampened_set=sequence[:i]+sequence[i+1:] 
        if checksafe(dampened_set):
            return True
    return False

for line in data:
    if line.strip(): 

        #map() function is used to apply a function to every item of an iterable
        #map meeds to be converted back to list
        sequence=list(map(int,line.split(' ')))

        #part1
        if checksafe(sequence):
            safe_sequences+=1

        #part 2
        if dampener(sequence):
            dampened_safe_sequence+=1

print(safe_sequences)
print(dampened_safe_sequence)