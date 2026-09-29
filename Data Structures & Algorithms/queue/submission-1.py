class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Deque:
    # Singly linked list with dummy head: dummy -> n0 -> ... -> n(size-1)
    # From dummy, k steps lands on n(k-1).
    # appendleft/popleft O(1), append/pop O(n)
    def __init__(self):
        self.head = Node(0)                # dummy
        self.size = 0

    def isEmpty(self) -> bool:
        return (self.size == 0)

    def append(self, value: int) -> None:
        # size steps -> last node (or dummy if empty)
        curr = self.head
        for i in range(self.size):
            curr = curr.next

        new_node = Node(value)
        curr.next = new_node
        self.size += 1

    def appendleft(self, value: int) -> None:
        new_node = Node(value)
        curr = self.head
        new_node.next = curr.next          # link to old first BEFORE moving dummy
        curr.next = new_node
        self.size += 1

    def pop(self) -> int:
        if self.size == 0:
            return -1

        # size-1 steps -> second-last node (need prev to cut the link)
        curr = self.head
        for i in range(self.size - 1):
            curr = curr.next

        last_node = curr.next
        curr.next = None
        self.size -= 1
        return last_node.val

    def popleft(self) -> int:
        if self.size == 0:
            return -1

        curr = self.head
        first_node = curr.next
        curr.next = curr.next.next         # dummy skips first node
        self.size -= 1
        return first_node.val