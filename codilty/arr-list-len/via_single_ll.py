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
