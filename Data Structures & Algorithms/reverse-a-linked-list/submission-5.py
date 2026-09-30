# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # RECURSION
        new_head = head

        if not head or not head.next:
            return head

        # ---------------------------------------------------------------
        # RECURSIVE STEP:
        #   Trust the recursion: "reverse everything AFTER me."
        #   new_head will be the last node (3), which is the new front.
        # ---------------------------------------------------------------
        new_head = self.reverseList(head.next)        

        # The two lines that do everything
        head.next.next = head # flip the arrow
        head.next = None # cut the old forward link to avoid a cycle

        return new_head

# EXPLANATION
# reverseList(1)
#    calls reverseList(2)
#       calls reverseList(3)
#          base case: 3.next is None -> return 3   ← new_head = 3


# Back in reverseList(2):   new_head = 3
#    2.next.next = 2   →   3.next = 2     (3 now points back to 2)
#    2.next = None     →   breaks 2 -> 3
#    return 3
#    List so far: 3 -> 2 -> None

# Back in reverseList(1):   new_head = 3
#    1.next.next = 1   →   2.next = 1     (2 now points back to 1)
#    1.next = None     →   breaks 1 -> 2
#    return 3
#    Final list: 3 -> 2 -> 1 -> None
