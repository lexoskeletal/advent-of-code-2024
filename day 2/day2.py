data=open('day2input.txt','r').read().split('\n')

safe_sequences=0
dampened_safe_sequence=0

def splitconvert(line, int_sequence):
    string_sequence=line.split(' ')
    for i in range(len(string_sequence)):
        int_sequence.append(int(string_sequence[i]))

def checksafe(int_sequence):

    #to check if sequence is increasing or decreasing
    increasing=False
    decreasing=False

    for i in range(len(int_sequence)-1):
        level_difference=int_sequence[i+1]-int_sequence[i]
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

def dampener(int_sequence):
    for i in range(len(int_sequence)):

        #delete an element, make copy
        dampened_set=int_sequence[:i]+int_sequence[i+1:] 
        if checksafe(dampened_set):
            return True
    return False


for line in data:
    if line.strip(): 
        int_sequence=[]
        splitconvert(line,int_sequence)
        #part1
        if checksafe(int_sequence):
            safe_sequences+=1

        #part 2
        if dampener(int_sequence):
            dampened_safe_sequence+=1


print(safe_sequences)
print(dampened_safe_sequence)