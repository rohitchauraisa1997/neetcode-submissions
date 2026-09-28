class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:
    # SINGLE LINKED LIST USING WHILE
    # self.head is a dummy (sentinel) node; real data starts at self.head.next.
    # The dummy means insert/delete at index 0 needs no special case:
    # there is always a "previous" node.
    # ** curr = self.head.next only in case of get method.
    def __init__(self):
        self.head = ListNode(0)
        self.size = 0

    def is_empty(self): # helper func
        return (self.size == 0)

    def print_ll(self): # helper func
        if not self.is_empty():
            curr = self.head.next              # skip dummy
            while curr:
                print(curr.val, end="->")
                curr = curr.next
            print("None")
        else:
            print("empty list")

    def get(self, index: int) -> int:
        # valid indices are 0..size-1
        if index >= self.size:
            return -1

        # start at the first real node; after `index` steps curr IS the target
        curr = self.head.next
        # `while curr` (not curr.next) so the loop can land on the last node
        while curr:
            if index == 0:                     # check BEFORE decrementing
                return curr.val
            index -= 1
            curr = curr.next

    def addAtHead(self, val: int) -> None:
        # insert right after the dummy
        new_node = ListNode(val)
        new_node.next = self.head.next         # link new node to old first node
        self.head.next = new_node              # dummy now points to new node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        curr = self.head
        while curr.next:
            curr = curr.next
        # above loop breaks at last node as curr.next is None
        curr.next = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        # valid indices are 0..size (index == size means append at tail)
        if index > self.size:
            return

        new_node = ListNode(val)
        # start at the dummy; after `index` steps curr is the node BEFORE the insert position
        curr = self.head

        # `while curr` (not curr.next): when index == size, the node before
        # the insert position is the tail, whose .next is None.
        # `while curr.next` would exit before checking index == 0.
        while curr:
            if index == 0:                     # check BEFORE decrementing
                new_node.next = curr.next      # new node points to old node at this index
                curr.next = new_node           # previous node points to new node
                self.size += 1
                return
            index -= 1
            curr = curr.next

    def deleteAtIndex(self, index: int) -> None:
        # valid indices are 0..size-1 (index == size falls through the loop harmlessly)
        if index > self.size:
            return

        # start at the dummy; after `index` steps curr is the node BEFORE the target
        curr = self.head
        # `while curr.next`: there must be a node after curr to delete.
        # Stopping at the tail is correct because there is nothing after it.
        while curr.next:
            if index == 0:                     # check BEFORE decrementing
                curr.next = curr.next.next     # bypass target; it gets garbage collected
                self.size -= 1
                return
            index -= 1
            curr = curr.next