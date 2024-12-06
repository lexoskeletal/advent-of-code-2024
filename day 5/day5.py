allrules,allupdatedpages=open('day5input.txt','r').read().strip().split("\n\n")

#using for separately overwrites allupdatedpages in each iteration
allupdatedpages=[list(map(int,line.split(","))) for line in allupdatedpages.split("\n")]

rules=[]
for line in allrules.split("\n"):
    part1, part2=line.split("|")
    rules.append((int(part1),int(part2)))

#part 1
def follows_rules(updatedpages):

    #dict of page and indices
    index={}
    for i, num in enumerate(updatedpages):
        index[num]=i

    for part1,part2, in rules:
        if part1 in index and part2 in index and not index[part1]<index[part2]:
            return False, 0
    
    return True, updatedpages[len(updatedpages)//2]


legalmidpagesum=0

#for part 2
incorrectpages=[]
for updatedpages in allupdatedpages:
    legal,midpage=follows_rules(updatedpages)
    if legal:
        legalmidpagesum+=midpage

    else:
        incorrectpages.append(updatedpages)

print(legalmidpagesum)

#part2
def bubble_sort_on_drugs(pages):

    while True:
        is_sorted=True
        for i in range(len(pages)-1):

            #out of order

            #only works if each page has a rule associated with all other pages 
            if((pages[i+1],pages[i]) in rules):
                is_sorted=False
                pages[i],pages[i+1]=pages[i+1],pages[i]
        
        if is_sorted:
            return pages[len(pages)//2]

correctedmidpagesum=0
for pages in incorrectpages:
    midpage=bubble_sort_on_drugs(pages)
    correctedmidpagesum+=midpage

print(correctedmidpagesum)