
def makeAdjMatrix(file_name):

    file_in = open(file_name, "r")
    nodes_N, edges_M = map(int, file_in.readline().split())

    adjMat = [[0 for _ in range(nodes_N+1)] for _ in range(nodes_N+1)]

    for i in range(edges_M):
        # u = int(input())
        # v = int(input())
        # w = int(input())

        u, v, w = map(int, file_in.readline().split())

        adjMat[u][v] = w

    return adjMat


def graphRepr(adjMat):
    file_out = open("output1A.txt", 'w')
    for i in adjMat:
        for j in i:
            file_out.write(f"{j} ")
        file_out.write(f"\n")
            

graph1 = makeAdjMatrix("input1a_1.txt")
graphRepr(graph1)
