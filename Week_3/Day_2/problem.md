# Maximum Sum Path in Binary Tree

## Description
Given a binary tree, implement a function that returns the maximum sum of a path from root to leaf.

## Examples

### Example 1
```
    17
   /  \
  3   -10
 /    /  \
2    16   1
         /
        13
```
**Expected output:** `23` (path: `17 -> -10 -> 16`)

### Example 2
```
        5
      /   \
    4      10
   / \     /
-80 -60 -90
```
**Expected output:** `-51` (path: `5 -> 4 -> -60`)

## Important Notes
- Return `0` if the tree is empty
- You must find the best possible route *from root to leaf*
- You cannot skip leaves - the path must end at a leaf node

## Tree Node Structure
```haskell
data TreeNode = None | Node TreeNode Int TreeNode
```

## Series Information
This kata is part of the "Fun with trees" series:
- Fun with trees: max sum
- Fun with trees: array to tree
- Fun with trees: is perfect

[Fun with trees: max sum](https://www.codewars.com/kata/57e5279b7cf1aea5cf000359)