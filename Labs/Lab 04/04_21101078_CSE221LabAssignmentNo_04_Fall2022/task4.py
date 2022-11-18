# Task : 04 Check if a graph is cyclic or not

# graph is Directed and unweighted

def makeGraph(file_name):

    file_in = open(file_name, "r")
    nodes_N, edges_M = map(int, file_in.readline().split())

    # key as node u -->value as  adjList[][] --> (v, color)
    adjDict = {}
    for i in range(1, nodes_N+1):
        adjDict[i] = [[],0]

    for i in range(1, edges_M+1):

        u, v = map(int, file_in.readline().split())

        # if adjDict.get(u) == None:
        #     adjDict[u] = [[],0]
        #     adjDict[u][0].append(v)
        # else:
        #     adjDict[u][0].append(v)

    return adjDict # Returning adjList as dict


# cycle checking using the DFS Algorithm

s = []


def DFS(graph, u):

    if len(graph[u][0]) == 0 and len(s) != 0:
        s.pop()
    if graph[u][1] == 0:
        if u not in s:
            s.append(u)
        else:
            return

        for v in graph[u][0]:
            return DFS(graph, v)

# ===============
graph2 = makeGraph("input4_2.txt")


def isCyclic(graph, u):

    DFS(graph, u)
    if (len(s) != 0):
        print("YES")
    else:
        print("NO")  

#===============================     
isCyclic(graph2, 1)