
l = []
n = int(input())
for i in range(n):
    task = list(map(int, input().split()))
    task.sort(reverse= True)
    l.append(task)

# print(l)
l.sort()


l2 = []

for i in range(n):
    if len(l2) == 0:
        l2.append(l[i])
    else:
        prev = l2[-1][0]

        if (prev <= l[i][-1]):
            l2.append(l[i])

print(len(l2))
for i in l2:
    print(i[1], i[0])