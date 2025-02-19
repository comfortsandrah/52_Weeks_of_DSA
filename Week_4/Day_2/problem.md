# Valid Path in a Graph

## Problem Statement

You are given a **bi-directional graph** with `n` vertices, labeled from `0` to `n - 1`. The edges of the graph are represented as a **2D integer array** `edges`, where `edges[i] = [ui, vi]` indicates a bi-directional edge between vertex `ui` and vertex `vi`.  
Each vertex pair has at most **one edge**, and no vertex has an edge to itself.  

Your task is to determine whether there is a **valid path** from a given `source` vertex to a `destination` vertex.  

### **Function Signature**
```python
def validPath(n: int, edges: List[List[int]], source: int, destination: int) -> bool:

## **Source of Problem**
[Leetcode Valid Path in a Graph](https://leetcode.com/problems/find-if-path-exists-in-graph/description/)
