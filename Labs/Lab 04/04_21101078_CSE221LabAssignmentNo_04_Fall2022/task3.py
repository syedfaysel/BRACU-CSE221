


# DFS Traversal : Dora the explorer
# graph is undirected and unweighted

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





# the DFS Algorithm

file_out = open("output3.txt", 'w')

def DFS(graph, u):

    if graph[u][1] == 0:
        file_out.write(f"{u} ")
        graph[u][1] = 1

        for v in graph[u][0]:
            DFS(graph, v)

# ===============
graph2 = makeGraph("input2_4.txt")
DFS(graph2, 1)
