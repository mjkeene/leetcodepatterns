# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        nxt = None

        while curr:
            curr_nxt = curr.next
            curr.next = nxt
            nxt = curr
            curr = curr_nxt

        return nxt
