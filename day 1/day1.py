data=open('day1input.txt','r').read().split('\n')

list1=[]
list2=[]
for line in data:
    if line.strip(): #skip empty lines
        column1,column2=line.split('   ')
        list1.append(int(column1))
        list2.append(int(column2))

#part 1
list1.sort()
list2.sort()

distance=0 
for i in range(1000):
    if list1[i]>list2[i]:
        distance=distance+(list1[i]-list2[i])
    else:
        distance+=list2[i]-list1[i]
    print(distance)
print(distance)

#part 2
frequency=0
similarity_score=0

for location_id in list1:
    if list2.count(location_id)>0:
        similarity_score+=location_id*list2.count(location_id)
    
print(similarity_score)