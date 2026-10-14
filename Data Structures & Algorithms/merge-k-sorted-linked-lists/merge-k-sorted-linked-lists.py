"""
Merge K Sorted Linked Lists (NeetCode)
======================================

You are given an array of k linked lists lists, where each list is sorted in
ascending order.

Return the sorted linked list that is the result of merging all of the
individual linked lists.

Example 1:
    Input:  lists = [[1,2,4],[1,3,5],[3,6]]
    Output: [1,1,2,3,3,4,5,6]

Example 2:
    Input:  lists = []
    Output: []

Example 3:
    Input:  lists = [[]]
    Output: []

Constraints:
    0 <= lists.length <= 1000
    0 <= lists[i].length <= 100
    -1000 <= lists[i][j] <= 1000
"""

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        # Merge in pairs; each round halves the list count, so ~log k rounds.
        # Merging one list at a time into a running result is O(N*k).
        while len(lists) > 1:
            # Results of this round: one merged list per pair, so about half as many lists.
            # It becomes `lists` for the next round.
            # e.g. [L0, L1, L2, L3, L4] -> [L0+L1, L2+L3, L4]
            mergedLists = []

            # Use len(lists) here. It shrinks every round, so don't store it once up front.
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None  # odd count: last list merges with None
                mergedLists.append(self.mergeTwoLinkedLists(l1, l2))  # keep inside the for loop
            lists = mergedLists

        return lists[0]

    def mergeTwoLinkedLists(self, l1, l2):
        dummy = ListNode()  # anchor that never moves; the real head is dummy.next
        tail = dummy        # last node of the merged list

        while l1 and l2:
            if l1.val <= l2.val:  # <= keeps equal values in their original order
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next  # forgetting this keeps overwriting dummy.next

        tail.next = l1 or l2  # attach the remaining nodes in one step, no loop needed
        return dummy.next     # not dummy

# Time: O(N log k), where N is the total number of nodes. Space: O(k).