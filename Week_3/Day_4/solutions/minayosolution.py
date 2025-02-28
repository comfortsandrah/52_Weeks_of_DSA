class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def insert(self, root, data):
        if root is None:
            return Node(data)
        elif data <= root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)
        return root

    def getHeight(self, root):
        if root is None:
            return -1  # Base case: empty tree has height -1
        left_height = self.getHeight(root.left)
        right_height = self.getHeight(root.right)
        return 1 + max(left_height, right_height)

# Read input
tree = Solution()
root = None
n = int(input())  # Number of nodes
for _ in range(n):
    data = int(input())
    root = tree.insert(root, data)

# Print output
print(tree.getHeight(root))
