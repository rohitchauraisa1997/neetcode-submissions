"""
ArrListLen (Codility)
=====================

A non-empty array A consisting of N integers is given. Array A represents a
linked list. A list is constructed from this array as follows:

    - the first node (the head) is located at index 0;
    - the value of a node located at index K is A[K];
    - if the value of a node is -1 then it is the last node of the list;
    - otherwise, the successor of a node located at index K is located at
      index A[K] (you can assume that A[K] is a valid index, that is
      0 <= A[K] < N).

For example, for array A such that:

    A[0] =  1
    A[1] =  4
    A[2] = -1
    A[3] =  3
    A[4] =  2

the following list is constructed:

    - the first node (the head) is located at index 0 and has a value of 1;
    - the second node is located at index 1 and has a value of 4;
    - the third node is located at index 4 and has a value of 2;
    - the fourth node is located at index 2 and has a value of -1.

Write a function:

def solution(A)

that, given a non-empty array A consisting of N integers, returns the length
of the list constructed from A in the above manner.

For example, given array A such that A = [1, 4, -1, 3, 2] the function should
return 4, as explained in the example above.

Assume that:

N is an integer within the range [1..200,000];
each element of array A is an integer within the range [-1..N-1];
it will always be possible to construct the list and its length will be
finite.
"""

# *** HITS TIMEOUT coz of push so use doublyLL***
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None         # singly linked: only a `next` pointer

class LinkedList:
    def __init__(self):
        self.head = Node(0)      # dummy/sentinel node, not counted in size
        self.size = 0

    def push(self, val):
        # NOTE: walks head -> end on every push = O(N) per push, O(N^2) total.
        #   Correct, but may time out on large Codility tests.
        curr = self.head
        for i in range(self.size):
            curr = curr.next
        curr.next = Node(val)
        self.size += 1

    def print_ll(self):
        curr = self.head.next
        for i in range(self.size):
            print(curr.val, end = "=>")
            curr = curr.next
        print()

    def size_of_ll(self):
        return self.size

def solution(A):
    if len(A)==0:
        return 0                 

    l = LinkedList()
    index = 0                    # start at the head (index 0)
    l.push(A[index])             # head node is always part of the list

    # FIX: follow the pointers until the current node's value is -1.
    while A[index] != -1:
        index = A[index]         # jump to the successor
        l.push(A[index])         # add that node's value

    # l.print_ll()                 # debug only; stdout is ignored in scoring
    return l.size_of_ll()        # Time: O(N^2) due to push, Space: O(N)
