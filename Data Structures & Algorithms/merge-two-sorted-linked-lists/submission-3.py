# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # RECURSIVE
        # Time complexity O(n+m)
        # Space complexity O(n+m)

        # BASE CASE 1: list1 is exhausted -> the rest of the merged list is just list2
        if list1 is None:
            return list2

        # BASE CASE 2: list2 is exhausted -> the rest of the merged list is just list1
        if list2 is None:
            return list1
        
        if list1.val < list2.val:
            # list1 wins this spot. Recurse with list1's remainder vs the whole list2.
            # Whatever comes back is appended right after list1.
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            # list2 wins this spot (ties go to list2, which is fine).
            list2.next = self.mergeTwoLists(list2.next, list1)
            return list2
        
# Let's trace list1 = [1, 2, 4] and list2 = [1, 3, 5].

# Call 1: merge([1,2,4], [1,3,5])
#   1 < 1? No  -> else branch: list2 (val=1) wins
#   list2.next = merge([1,2,4], [3,5])   <- note list2 advanced
#   return list2 (val=1)

#   Call 2: merge([1,2,4], [3,5])
#     1 < 3? Yes -> list1 (val=1) wins
#     list1.next = merge([2,4], [3,5])
#     return list1 (val=1)

#     Call 3: merge([2,4], [3,5])
#       2 < 3? Yes -> list1 (val=2) wins
#       list1.next = merge([4], [3,5])
#       return list1 (val=2)

#       Call 4: merge([4], [3,5])
#         4 < 3? No -> else: list2 (val=3) wins
#         list2.next = merge([4], [5])
#         return list2 (val=3)

#         Call 5: merge([4], [5])
#           4 < 5? Yes -> list1 (val=4) wins
#           list1.next = merge([], [5])
#           return list1 (val=4)

#           Call 6: merge([], [5])
#             BASE CASE: list1 is None -> return list2 ([5])

#     Unwinding the stack (each call attaches its result to .next):

#     Call 5 returns: 4 -> 5
#     Call 4 returns: 3 -> 4 -> 5
#     Call 3 returns: 2 -> 3 -> 4 -> 5
#     Call 2 returns: 1 -> 2 -> 3 -> 4 -> 5
#     Call 1 returns: 1 -> 1 -> 2 -> 3 -> 4 -> 5