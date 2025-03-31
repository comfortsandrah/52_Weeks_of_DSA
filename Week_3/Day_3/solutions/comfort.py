from preloaded import Node


def array_to_tree(arr):
    if not arr:
        return None
    nodes = []
    for i in range(len(arr)):       
        nodes.append(Node(arr[i]))
        
    for i in range(len(nodes)):
        left_index   = 2 * i + 1
        right_index  = 2 * i + 2
        if left_index < len(nodes):
            nodes[i].left = nodes[left_index]
        if right_index < len(nodes):
            nodes[i].right = nodes[right_index]
            
    return nodes[0]       