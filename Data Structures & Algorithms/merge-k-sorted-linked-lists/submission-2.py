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