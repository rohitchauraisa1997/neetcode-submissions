"""
Design Linked List (NeetCode)
=============================

Design your implementation of the linked list. You can choose to use a singly
or doubly linked list.

A node in a singly linked list should have two attributes: val and next. val is
the value of the current node, and next is a pointer/reference to the next
node. If you want to use the doubly linked list, you will need one more
attribute prev to indicate the previous node in the linked list. Assume all
nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:
    - MyLinkedList() Initializes the MyLinkedList object.
    - int get(int index) Get the value of the indexth node in the linked list.
      If the index is invalid, return -1.
    - void addAtHead(int val) Add a node of value val before the first element
      of the linked list. After the insertion, the new node will be the first
      node of the linked list.
    - void addAtTail(int val) Append a node of value val as the last element of
      the linked list.
    - void addAtIndex(int index, int val) Add a node of value val before the
      indexth node in the linked list. If index equals the length of the
      linked list, the node will be appended to the end of the linked list. If
      index is greater than the length, the node will not be inserted.
    - void deleteAtIndex(int index) Delete the indexth node in the linked list,
      if the index is valid.

Example 1:
    Input:  ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get",
             "deleteAtIndex", "get"]
            [[], [1], [3], [1, 2], [1], [1], [1]]
    Output: [null, null, null, null, 2, null, 3]

    Explanation:
    MyLinkedList myLinkedList = new MyLinkedList();
    myLinkedList.addAtHead(1);
    myLinkedList.addAtTail(3);
    myLinkedList.addAtIndex(1, 2);  // linked list becomes 1->2->3
    myLinkedList.get(1);            // return 2
    myLinkedList.deleteAtIndex(1);  // now the linked list is 1->3
    myLinkedList.get(1);            // return 3

Constraints:
    0 <= index, val <= 1000
    Please do not use the built-in LinkedList library.
    At most 2000 calls will be made to get, addAtHead, addAtTail, addAtIndex
    and deleteAtIndex.
"""

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