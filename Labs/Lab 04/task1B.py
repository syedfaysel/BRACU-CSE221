

def makeAdjList(file_name):

    file_in = open(file_name, "r")
    nodes_N, edges_M = map(int, file_in.readline().split())

    adjList = [[] for _ in range(nodes_N+1)]

    for i in range(edges_M):

        u, v, w = map(int, file_in.readline().split())

        adjList[u].append((v,w))

    return adjList


def graphRepr(adjList):

    file_out = open("output1B.txt", 'w')
    for i in range(len(adjList)):
        file_out.write(f"{i} : ")
        for j in adjList[i]:
            file_out.write(f"{j} ")
        file_out.write(f"\n")
            
#=============================
graph1 = makeAdjList("input1b_3.txt")
graphRepr(graph1)
