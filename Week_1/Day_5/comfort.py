def alternating_split(head):
    if not head or not head.next:
        raise ValueError("List must contain at least two nodes.")
    
    first_head = head  # First list starts with head
    second_head = head.next  # Second list starts with next node
    
    first_tail = first_head
    second_tail = second_head
    
    current = second_head.next  # Move to third node (if exists)
    is_first = True  # Toggle flag for alternating nodes
    
    while current:
        if is_first:
            first_tail.next = current
            first_tail = first_tail.next
        else:
            second_tail.next = current
            second_tail = second_tail.next
        
        current = current.next  # Move to next node
        is_first = not is_first  # Toggle the flag
    
    # Terminate the two lists
    first_tail.next = None
    second_tail.next = None
    
    return (first_head, second_head)