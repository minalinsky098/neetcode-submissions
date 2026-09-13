# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        node_head = head
        prev = None
        curr = head
        while curr.next:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        else:
            node_head = curr
            node_head.next = prev
            
        return node_head
        