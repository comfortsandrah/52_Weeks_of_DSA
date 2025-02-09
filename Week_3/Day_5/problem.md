# Lowest Common Ancestor in Binary Tree

## Description
Given a binary tree and two nodes `p` and `q`, find their lowest common ancestor (LCA). The LCA is defined as the lowest node in the tree that has both `p` and `q` as descendants, where a node can be a descendant of itself.

## Examples

### Example 1
```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
```

### Example 2
```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5 (a node can be a descendant of itself)
```

### Example 3
```
Input: root = [1,2], p = 1, q = 2
Output: 1
```

## Constraints
- Number of nodes: `2 ≤ n ≤ 105`
- Node values: `-109 ≤ Node.val ≤ 109`
- All node values are unique
- `p ≠ q`
- Both `p` and `q` exist in the tree
- A node can be a descendant of itself

[Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/)