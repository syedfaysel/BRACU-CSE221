
## Hospital management system

# Way 1: using bubble sort

queue = []

def enque(item):
    # token = int(item[-1])
    queue.append(item)
    # using bubble Sort
    for i in range(len(queue)-1):
        for j in range(len(queue) - i -1):
            if queue[j][-1] > queue[j+1][-1]:
                # swap 
                queue[j], queue[j+1] = queue[j+1], queue[j]  

def seeDoctor():
    if len(queue)<1:
        return None
    print(queue.pop(0))

def printQueue():
    print(queue)


with open("input4.txt", "r") as file_in:


    temp = file_in.read().splitlines()

    for i in temp:
        if i == 'see doctor':
            seeDoctor()
        else:
            enque(i)
    



