from collections import defaultdict

class Graph:
    def __init__(self,vertices):
        self.noOfVertex = vertices
        self.graph = defaultdict(list)

    def addEdge(self,start,end):
        self.graph[start].append(end)

    def search(self,src,target,maxDepth):
        if src == target:
            return True
        
        if maxDepth<=0:
            return False
        
        for i in self.graph[src]:
            if self.search(i,target,maxDepth-1):
                return True
        
        return False

    def iterativeSearch(self,src,target,maxDepth):
        for i in range(maxDepth):
            if self.search(src,target,i):
                return True
        
        return False

if __name__ == "__main__":
    print("Enter number of vertex: ",end="")
    n = int(input())

    g = Graph(n)

    print("Enter no of edges: ",end="")
    noOfEdge = int(input())

    print("Enter edges: ")

    for i in range(noOfEdge):
        edge = list(map(int, input().split(" ")))
        g.addEdge(edge[0],edge[1])

    print("Enter src vertex: ",end="")
    src = int(input())

    print("Enter target vertex: ",end="")
    target = int(input())

    print("Enter maxDepth: ",end="")
    maxDepth = int(input())

    if g.iterativeSearch(src,target,maxDepth):
        print("Can reach")
    else:
        print("Cannot reach")