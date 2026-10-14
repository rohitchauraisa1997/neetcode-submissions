# ---------------------------------------------------------------------------
# PROBLEM: Length of a linked list stored in an array  (Codility)
#
# A non-empty array A of N integers represents a linked list:
#   - the head node is at index 0
#   - the value of the node at index K is A[K]
#   - if the value is -1, that node is the last node (tail)
#   - otherwise the successor of node K is at index A[K]
#     (A[K] is always a valid index: 0 <= A[K] < N)
#
# Task: return the length of the list (number of nodes).
#
# EXAMPLE:
#   A[0] =  1
#   A[1] =  4
#   A[2] = -1
#   A[3] =  3
#   A[4] =  2
#
#             +-------------------+
#        +--+ |          +------+ |
#        |  v |          |      v |
#   A: [ 1 | 4 | -1 | 3 | 2 ]
#        0   1    2    3   4
#                 ^         |
#                 +---------+
#
#   The following list is constructed:
#   index: 0  ->  1  ->  4  ->  2
#   value: 1      4      2     -1 (tail)
#
#   Node at index 3 is never reached (not part of the list).
#   Answer = 4
#
# EDGE CASE: A = [-1]  -> head is also tail -> answer = 1
# ---------------------------------------------------------------------------

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Guard: spec says A is non-empty, but handle it defensively
    if len(A)==0:
        return 0

    index = 0   # start at the head node (index 0)
    lenLl = 1   # head always exists, so count it

    # Follow successor pointers until we reach the tail (value -1)
    while A[index]!=-1:
        lenLl += 1          # moving to the next node adds one to the length
        index = A[index]    # successor of node at `index` is at A[index]

    # Time: O(N), each node visited once; Space: O(1)
    return lenLl
