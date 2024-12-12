"""
itertools: creating iterators to simplify
operations involving loops, combinations, permutations, and 
cartesian products

"""
from itertools import product
from tqdm import tqdm

raw_equations=open('day7input.txt','r').read().strip().split("\n")

def solve(combo, numbers):

    result=numbers[0]
    for i in range(1,len(numbers)):

        #check first operation b/w first two numbers and so on
        if combo[i-1]=="+":
            result+=numbers[i]
        
        #for part 2
        elif combo[i-1]=="|":
            result=int(f"{result}{numbers[i]}")
                       
        else:
            result*=numbers[i]

    return result


calibration_result=0

for line in raw_equations:
    parts=line.split()

    #slicing away colon from the end
    target_value=int(parts[0][:-1])
    numbers=list(map(int, parts[1:]))

    #cartesian product of *+| with itself to create 
    #possible combos of operators
    for combo in product("*+|", repeat=len(numbers)-1):
        if solve(combo, numbers)==target_value:
            calibration_result+=target_value

            #break if combo fits
            break

print(calibration_result)
