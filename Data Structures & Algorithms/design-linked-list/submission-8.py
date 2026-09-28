class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:
    # doubly LL
    def __init__(self):
        self.left = Node(0)            # left sentinel (dummy head)
        self.right = Node(0)           # right sentinel (dummy tail)
        self.left.next = self.right
        self.right.prev = self.left        

    def get(self, index: int) -> int:
        curr = self.left.next          # first real node

        while curr and index>0:
            index -= 1
            curr = curr.next

        # must exclude right sentinel (its val is a placeholder)
        if curr and curr!= self.right: 
            return curr.val
        return -1

    def addAtHead(self, val: int) -> None:
        new_node, next, prev = Node(val), self.left.next, self.left
        new_node.next = next
        new_node.prev = prev
        next.prev = new_node
        prev.next = new_node

    def addAtTail(self, val: int) -> None:
        # right sentinel gives O(1) access to the tail
        new_node, next, prev = Node(val), self.right, self.right.prev
        new_node.next = next
        new_node.prev = prev
        next.prev = new_node
        prev.next = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.left.next
        while curr and index>0:
            index -= 1
            curr = curr.next

        # index==0 means we landed on target; curr.prev gives predecessor in O(1)
        if curr and index==0:
            new_node, next, prev = Node(val), curr, curr.prev
            new_node.next = next
            new_node.prev = prev
            next.prev = new_node
            prev.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        curr = self.left.next
        while curr and index>0:
            index -= 1
            curr = curr.next    

        # extra curr != self.right: can't delete a sentinel
        if curr and curr != self.right and index==0:
            next, prev = curr.next, curr.prev
            next.prev = prev
            prev.next = next