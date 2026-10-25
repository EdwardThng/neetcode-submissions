# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        current = slow.next
        slow.next = None
        prev = None

        while current:
            Next = current.next
            current.next = prev
            prev = current
            current = Next

        curr1 = head
        curr2 = prev
        
        while curr2:
            NextNode1 = curr1.next
            NextNode2 = curr2.next
            curr1.next = curr2
            curr2.next = NextNode1
            curr1 = NextNode1
            curr2 = NextNode2
        return 
