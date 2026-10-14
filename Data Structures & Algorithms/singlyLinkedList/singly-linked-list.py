"""
Design Singly Linked List (NeetCode)
====================================

Design a Singly Linked List class.

Your LinkedList class should support the following operations:
    - LinkedList() will initialize an empty linked list.
    - int get(int i) will return the value of the ith node (0-indexed). If the
      index is out of bounds, return -1.
    - void insertHead(int val) will insert a node with val at the head of the
      list.
    - void insertTail(int val) will insert a node with val at the tail of the
      list.
    - bool remove(int i) will remove the ith node (0-indexed). If the index is
      out of bounds, return false, otherwise return true.
    - int[] getValues() return an array of all the values in the linked list,
      ordered from head to tail.

Example 1:
    Input:  ["insertHead", 1, "insertTail", 2, "insertHead", 0, "remove", 1,
             "getValues"]
    Output: [null, null, null, true, [0, 2]]

Example 2:
    Input:  ["insertHead", 1, "insertHead", 2, "get", 5]
    Output: [null, null, -1]

Note:
    The index int i provided to get(int i) and remove(int i) is guaranteed to
    be greater than or equal to 0.
"""

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node(0)
        self.size = 0
    
    def get(self, index: int) -> int:
        if self.size <= index:
            return -1

        curr = self.head.next
        for i in range(index):
            curr = curr.next
        return curr.val

    def insertHead(self, val: int) -> None:
        curr = self.head
        new_node = Node(val)
        new_node.next = curr.next
        curr.next = new_node
        self.size += 1

    def insertTail(self, val: int) -> None:
        curr = self.head
        for i in range(self.size):
            curr = curr.next
        
        new_node = Node(val)
        curr.next = new_node
        self.size += 1

    def remove(self, index: int) -> bool:
        if self.size <= index:
            return False

        curr = self.head
        for i in range(index):
            curr = curr.next
        curr.next = curr.next.next
        self.size -= 1

        return True

    def getValues(self) -> List[int]:
        ans = []
        curr = self.head.next
        for i in range(self.size):
            ans.append(curr.val)
            curr = curr.next

        return ans
