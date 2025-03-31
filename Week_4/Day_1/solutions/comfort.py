from typing import List

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:        
        return  next(node for node in edges[0] if node in edges[1])
        