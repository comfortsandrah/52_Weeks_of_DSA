# Array to Complete Binary Tree

## Description
Implement a function that creates a complete binary tree from an array of integers. The elements should be inserted left-to-right, top-to-bottom.

A complete binary tree means every level, except possibly the last, is completely filled.

## Example
Given array: `[17, 0, -4, 3, 15]`

Resulting tree:
```
    17
   /  \
  0   -4
 / \
3   15 
```

## Implementation Details
The elements should be:
- Taken from the array left-to-right
- Inserted into the tree top-to-bottom, left-to-right

## Tree Node Structure
```haskell
data TreeNode = None | Node TreeNode Int TreeNode
```

## Series Information
This kata is part of the "Fun with trees" series:
- Fun with trees: max sum
- Fun with trees: array to tree
- Fun with trees: is perfect

[Fun with trees: array to tree](https://www.codewars.com/kata/57e5a6a67fbcc9ba900021cd)