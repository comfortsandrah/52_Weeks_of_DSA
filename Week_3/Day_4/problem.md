# Binary Search Tree Height Calculator

## Objective
Calculate the height of a Binary Search Tree (BST) - the number of edges between the tree's root and its furthest leaf.

## Task
Complete the `getHeight` function to return the height of the given binary search tree.

## Input Format
- First line: Integer `n` - number of nodes in the tree
- Next `n` lines: Integer values to be added to the BST

## Example

### Sample Input
```
7
3
5
2
1
4
6
7
```

### Sample Output
```
3
```

### Visual Representation
The input creates this BST:
```
     3
    / \
   2   5
  /   / \
 1   4   6
          \
           7
```

The longest root-to-leaf path (3 -> 5 -> 6 -> 7) has 3 edges, so the height is 3.

[Binary Search Trees](https://www.hackerrank.com/challenges/30-binary-search-trees/problem)