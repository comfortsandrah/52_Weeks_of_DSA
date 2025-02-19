# Maximum Star Sum in a Graph

## Problem Statement

You are given an **undirected graph** consisting of `n` nodes, **numbered from `0` to `n - 1`**. Each node has an associated value given by an integer array `vals` of length `n`, where `vals[i]` represents the value of node `i`.

You are also given a **2D integer array** `edges`, where `edges[i] = [a_i, b_i]` denotes that an **undirected edge** exists between nodes `a_i` and `b_i`.

### **Star Graph Definition**
A **star graph** is a subgraph of the given graph where:
- A **center node** connects to **0 or more neighbors**.
- The star consists of a subset of edges where there exists a **single central node** connected to all included edges.

The **star sum** is the sum of the values of **all nodes** in a given star graph.

### **Objective**
Given an integer `k`, return the **maximum star sum** of a star graph that contains **at most `k` edges**.

---

## **Examples**

### **Example 1**
#### **Input**
```python
vals = [1,2,3,4,10,-10,-20]
edges = [[0,1],[1,2],[1,3],[3,4],[3,5],[3,6]]
k = 2

## **Source of Problem**
[Leetcode Maximum Star Sum in a Graph](https://leetcode.com/problems/maximum-star-sum-of-a-graph/description/)
