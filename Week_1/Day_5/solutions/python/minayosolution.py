class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class Context:
    def __init__(self):
        self.first = None
        self.second = None

def alternatingSplit(head):
    if not head or not head.next:
        raise ValueError("The list must contain at least two nodes.")

    context = Context()
    current = head
    toggle = True  

    
    first_dummy = ListNode()
    second_dummy = ListNode()
    
    first_tail = first_dummy
    second_tail = second_dummy

    while current:
        if toggle:
            first_tail.next = current
            first_tail = first_tail.next
        else:
            second_tail.next = current
            second_tail = second_tail.next
        toggle = not toggle  
        current = current.next

    
    first_tail.next = None
    second_tail.next = None

    
    context.first = first_dummy.next
    context.second = second_dummy.next

    return context

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
result = alternatingSplit(head)


def print_list(node):
    while node:
        print(node.value, end=" -> ")
        node = node.next
    print("None")

print("First list:")
print_list(result.first)  

print("Second list:")
print_list(result.second)  