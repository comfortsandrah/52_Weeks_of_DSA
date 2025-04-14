class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(node):
    # If the input node is None (empty graph), just return None
    if node is None:
        return None
    
    # This dictionary keeps track of already copied nodes.
    # Key = original node, Value = copied node
    copied_nodes = {}

    # Define a helper function that uses DFS to copy nodes
    def dfs(original_node):
        # If the current node has already been copied, return the copy
        if original_node in copied_nodes:
            return copied_nodes[original_node]
        
        # Create a new copy of the current node (same value, empty neighbors for now)
        copy = Node(original_node.val)
        
        # Save this copy in the map so we don't duplicate or loop forever
        copied_nodes[original_node] = copy

        # Recursively copy all the neighbors of the original node
        for neighbor in original_node.neighbors:
            # Append the copied version of each neighbor to the new node's neighbors list
            copy.neighbors.append(dfs(neighbor))

        # Return the fully copied node
        return copy

    # Start the DFS cloning process from the given input node
    return dfs(node)
