

from os import stat
import queue
from xml.etree.ElementTree import iselement


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
        
        
    def bfs(self,start=0):
        class Queue:
            def __init__(self):
                self.q = []
            def insert(self,value):
                self.q.append(value)
            def front(self):
                return self.q.pop(0)
            def isEmpty(self):
                return len(self.q)==0
        visited = [False for _ in range(self.count)]
        queue = Queue()
        queue.insert(start)
        visited[start] = True
        while not queue.isEmpty():
            curr_node = queue.front()
            print(curr_node)
            for node in self.graph[curr_node]:
                if visited[node]==True:
                    continue
                queue.insert(node)
                visited[node] = True
                
edges = [(0,1),(0,2),(0,4),(1,2),(1,3),(2,3)]
graph = Graph(edges,13)

graph.bfs()
