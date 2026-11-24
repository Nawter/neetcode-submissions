# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []
        curr = head
        # transverse the linked list and push every node into an array
        while curr:
            nodes.append(curr)
            curr = curr.next
        
        # create the index diff between size of array and n
        remove_index = len(nodes) - n
        # if index is zero return head.next
        if remove_index == 0:
            return head.next
        
        # connect n-1.next to n.next
        nodes[remove_index - 1].next = nodes[remove_index].next

        # return the head
        return head

        