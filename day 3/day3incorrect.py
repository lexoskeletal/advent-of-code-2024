#this solution is incorrect but no clue why

import re
data=open('day3input.txt','r').read()
sum=0
sumconditional=0

#\d indicated digit sequence with 1-3 digits
#\( indicated match to literal "(" instead of grouping
# second ( captures only the digits

uncorrupted=re.findall(r"mul\((\d{1,3}),(\d{1,3})\)",data)
print(uncorrupted)

def multiplysum(uncorrupted,sumofproducts):
    for instruction in uncorrupted:
        sumofproducts+=int(instruction[0])*int(instruction[1])
    return sumofproducts

sum=multiplysum(uncorrupted,sum)
print(sum)

conditional=re.split(r"do\(\)", data)
for phrase in conditional:
    remove=re.sub(r"don't\(\).*","",phrase) #remove bad multiplicands
    goodmultiplicands=re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", remove)
    sumconditional=multiplysum(goodmultiplicands,sumconditional)

print(sumconditional)