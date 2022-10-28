
## Hospital management system

queue = []

def enque(item):
    token = int(item[-1])
    queue.append(item)
    for i in range(len(queue)):

        if token < int(queue[i][-1]):
            for j in range(len(queue)-1,i,-1):
                queue[j] = queue[j-1]
            queue[i-1] = item

def seeDoctor():
    if len(queue)<1:
        return None
    print(queue.pop(0))

def printQueue():
    print(queue)


with open("input4.txt", "r") as fp:
    while(True):
        try:
            inp = fp.readline()
            print(inp)
            # if inp == "see doctor":
            #     seeDoctor()
            # else:
            #     enque(inp)
        except EOFError:
            # lines_str = '\n'.join(lines)
            # print(lines_str)

            break


