

# Shortest Path

file_in = open("input5.txt", 'r')
file_out = open("output5.txt","w")

v, e , x = map(int, file_in.readline().split())

dict1 = {}
dict2 = {}
dict3 = {}

for i in range(1,v+1):
    dict1[i]=[]
    dict2[i]=0
    dict3[i]=0

for i in range(e):
    key, value = map(int, file_in.readline().split())

    if key in dict1.keys():
        if value not in dict1[key]:
            dict1[key].append(value)

    if value in dict1.keys():
        if key not in dict1[value]:
            dict1[value].append(key)

queue = [1]
visited = []

while queue:
    v = queue.pop(0)
    visited.append(v)

    for i, j in dict1.items():
        if i == v:
            for k in dict1[i]:
                if k not in queue:
                    if k not in visited:
                        queue.append(k)

                if dict2[k] == 0:
                    if k != 1:
                        dict2[k] = (dict2[v] + 1)
                        dict3[k] = i
final = [x]         
file_out.write("Time: "+str(dict2[x])+"\n")

while True:
    a = dict3.get(find)
    if a!=0:
        final.append(a)
    else:
        break
    find=a

for i in range(len(final)-1,-1,-1):
    file_out.write(str(final[i])+" ")