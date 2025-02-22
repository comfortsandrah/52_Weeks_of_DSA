# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root):
        def traverse(node):
            if node:
                return traverse(node.left) + [node.val] + traverse(node.right)
            return []
        
        return traverse(root)

