from preloaded import TreeNode

def max_sum(root: TreeNode) -> int:
    if not root:
        return 0
    if not root.left and not root.right:
        return root.value
    if not root.left:
        return max_sum(root.right) + root.value
    if not root.right:
        return max_sum(root.left) + root.value
    return max(max_sum(root.right),max_sum(root.left)) + root.value