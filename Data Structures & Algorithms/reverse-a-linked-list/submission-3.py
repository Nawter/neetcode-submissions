# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # we need the list element in the list
        prev, curr = None, head
 

        if head:
            following = head.next
 
        while curr:
            curr.next = prev
            prev = curr
            curr = following
            if following:
                following = following.next

        return prev
        


        