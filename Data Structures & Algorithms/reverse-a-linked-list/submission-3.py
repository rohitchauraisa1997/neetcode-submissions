# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # ITERATIVE using TWO pointers
        prev = None
        curr = head

        while curr:
            # stage the next node BEFORE we overwrite curr.next,
            # otherwise we lose the rest of the list.
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # when curr is None, the loop is done.
        # prev now sits on the original LAST node = new front.
        return prev