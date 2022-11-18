


# BFS Traversal : Dora the explorer
# graph is undirected and unweighted
# let's solve using dictionary this time


# so far my best approach to make a graph (undirected graph)
def makeGraph(file_name):

    file_in = open(file_name, "r")
    nodes_N, edges_M = map(int, file_in.readline().split())

    # key as node u -->value as  adjList[][] --> (v, color)
    adjDict = {}

    for i in range(1, edges_M+1):

        u, v = map(int, file_in.readline().split())

        if adjDict.get(u) == None:
            adjDict[u] = [[],0]
            adjDict[u][0].append(v)
        else:
            adjDict[u][0].append(v)

        if adjDict.get(v) == None:
            adjDict[v] = [[],0]
            adjDict[v][0].append(u)
        else:
            adjDict[v][0].append(u)


    return adjDict # Returning adjList as dict


# the BFS Algorithm (with the help of queue)

def BFS(graph, start):

    q = []
    # adjDict as graph
    graph[start][1] = 1
    q.append(start)

    file_out = open("output2.txt", 'w')
    while len(q) > 0:
        u = q.pop(0)
        file_out.write(f"{u} ")

        for v in graph[u][0]:
            if graph[v][1] == 0:
                graph[v][1] = 1
                q.append(v)

# ===============
graph2 = makeGraph("input2_4.txt")
BFS(graph2, 1)


