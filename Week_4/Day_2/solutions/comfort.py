from typing import List
from collections import deque

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = {}
        visited = set([source])
        queue = deque([source])

        for u,v in edges:
            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []
            graph[u].append(v)
            graph[v].append(u)        
     
        while queue:
            node = queue.popleft()
            if node == destination: 
                return True

            for neighbour in graph[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)
        return False


        
        
       
        
        