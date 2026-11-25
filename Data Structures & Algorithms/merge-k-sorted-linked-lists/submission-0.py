# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # create empty list nodes
        nodes = []
        # for each linked list
        # trasverse it and append every node value to nodes.
        for lst in lists:
            while lst:
                nodes.append(lst.val) 
                lst = lst.next                        
        # sort nodes
        nodes.sort()
        # create new list
        new_list = ListNode(0)
        # use dummy head
        dummy = new_list
        # for each value in the sorted list , create new node and attach it 
        for node in nodes:
            dummy.next = ListNode(node)
            dummy = dummy.next
        # return head of the new merged linked list
        return new_list.next
