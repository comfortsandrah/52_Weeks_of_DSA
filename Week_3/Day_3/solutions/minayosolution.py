class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Solution:
    def createCompleteBinaryTree(self, arr):
        if not arr:  
            return None
        
        # Create the root of the tree
        root = Node(arr[0])
        queue = [root]
        index = 1 
        while queue and index < len(arr):
            current = queue.pop(0)  
            # Insert the left child
            if index < len(arr):
                current.left = Node(arr[index])
                queue.append(current.left) 
            
            # Insert the right child
            if index < len(arr):
                current.right = Node(arr[index])
                queue.append(current.right)  # Add the right child to the queue
                index += 1
        
        return root
