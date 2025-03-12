# Clone Graph

## Problem Statement

You are given a **reference** to a node in a **connected, undirected graph**. Your task is to return a **deep copy (clone)** of the graph.

Each node in the graph has:
- A **value** (`int`).
- A **list of neighbors** (`List[Node]`).

The graph is represented using an **adjacency list** format.

### **Node Definition**
```java
class Node {
    public int val;
    public List<Node> neighbors;
}

## **Source of Problem**
[Leetcode Clone Graph](https://leetcode.com/problems/clone-graph/description/)
