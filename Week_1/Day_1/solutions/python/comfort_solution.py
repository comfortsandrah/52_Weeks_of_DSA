from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getMiddleElement(self,head: Optional[ListNode])->ListNode:
        hare= tortoise = head
        while hare and hare.next:
            tortoise = tortoise.next
            hare = hare.next.next
        return tortoise
    
    def reverseLinkedList(self, start: Optional[ListNode])->ListNode:
        current=next = start
        prev = None
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev  
            

    def isPalindrome(self, head: Optional[ListNode]) -> bool:        
        middleElement = self.getMiddleElement(head)
        reversedLinkedList = self.reverseLinkedList(middleElement)

        while head and reversedLinkedList:        
            if head.val!= reversedLinkedList.val:
                return False
            head = head.next
            reversedLinkedList = reversedLinkedList.next
        return True
    