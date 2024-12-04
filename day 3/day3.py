import re
data=open('day3input.txt','r').read()

#part 1
sumofproducts=0

#\d indicated digit sequence with 1-3 digits
#\( indicated match to literal "(" instead of grouping
# second ( captures only the digits
multiplicands=re.findall(r"mul\((\d{1,3}),(\d{1,3})\)",data)

for number in multiplicands:
    sumofproducts+=int(number[0])*int(number[1])

print(sumofproducts)

#part 2
#?: is a non-capturing group
conditional=re.findall(r"(?:mul\((\d{1,3}),(\d{1,3})\))|(do\(\)|don't\(\))", data)

sumconditional=0
enabled=True
for number in conditional:
    if number[2]== "" and enabled:
        sumconditional+=int(number[0])*int(number[1])
    else:
        if number[2]=="do()":
            enabled=True
        else:
            enabled=False

print(sumconditional)