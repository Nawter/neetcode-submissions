# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node that point to the head
        dummy = ListNode(0, head)
        
        # Create left and right nodes, left point to dummy, and right point to head
        left, right = dummy, head
      
        # move the right node, n steps forward
        for _ in range(n):
            right = right.next

        # move left and right until right reach the end
        while right:
            left = left.next
            right = right.next

        # left.next point at the node to skip, so we point it to left.next.next
        left.next = left.next.next

        # return dummy.next because it's always right 
        return dummy.next
        