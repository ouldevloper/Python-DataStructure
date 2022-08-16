

class Graph:
    def __init__(self,edges=[],count=0):
        self.edges = edges
        self.count = len(edges)
        self.graph = [[] for _ in range(self.count)]
        for edge in self.edges:
            self.graph[edge[0]].append(edge[1])
            self.graph[edge[1]].append(edge[0])
        
        for i in self.graph:
            print(i)
        
   
                
edges = [(0,1),(0,2),(0,4),(1,2),(1,3),(2,3)]
graph = Graph(edges,13)

