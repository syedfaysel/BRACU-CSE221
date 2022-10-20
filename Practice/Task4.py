# Task 4 : Rank the students

# n = int(input())
# ids = list(map(int, input().split()))
# marks = list(map(int, input().split()))

ids = [7,4,9,3,2,5,1]
marks = [40, 50, 50, 20, 10, 10, 10]

newDict = {}

for i in range(len(ids)):
    if newDict.get(marks[i]) == None:
        newDict[marks[i]] = [ids[i]]
    else:
        newDict[marks[i]].append(ids[i])



# Sorting by marks

def ins_sort(array):
    
    for j in range(1, len(array)):
        key = array[j]
        i = j-1
        
        while(i>=0 and array[i]>key):
            
            array[i+1] = array[i]  
            i = i-1
        array[i+1] = key


ins_sort(marks)

unique = []
for i in marks:
    if i not in unique:
        unique.append(i)



for key,value in newDict.items():
    temp = newDict[key]
    ins_sort(temp)
    newDict[key] = temp



for m in range(len(unique)-1, 0,-1):
    
    i_d = newDict[unique[m]]
    if len(i_d) == 0:

        print(f"ID: {i_d[0]} Mark: {unique[m]}")
    
    else:
        for x in range(len(i_d)):
            print(f"ID: {i_d[x]} Mark: {unique[m]}")





print(unique)






