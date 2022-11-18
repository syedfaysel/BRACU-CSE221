
def listGraph():
    with open("graph.txt","r") as f:
        n = int(f.readline())
        list_graph = [[] for _ in range(n)]
    
        c = int(f.readline())
    
        for i in range(c):
            line = f.readline()
            a, b = map(int, line.split(',') )
            print(a,b)
            
            list_graph[a-1].append(b)
    print(list_graph)
    
listGraph()