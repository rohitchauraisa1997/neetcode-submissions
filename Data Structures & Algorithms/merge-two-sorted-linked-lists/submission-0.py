# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # ITERATIVE
        # Time complexity O(n+m)
        # Space complexity O(1)

        dummy = node = ListNode()
        
        while list1 and list2:
            if list1.val < list2.val:
                node.next = ListNode(list1.val)
                list1 = list1.next
            else:
                node.next = ListNode(list2.val)
                list2 = list2.next
            node = node.next

        node.next = list1 or list2

        return dummy.next