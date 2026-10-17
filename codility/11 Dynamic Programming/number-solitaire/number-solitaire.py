"""
NumberSolitaire (Codility)

A game for one player is played on a board consisting of N consecutive squares,
numbered from 0 to N - 1. There is a number written on each square. A non-empty
array A of N integers contains the numbers written on the squares. Moreover, some
squares can be marked during the game.

At the beginning of the game, there is a pebble on square number 0 and this is the
only square on the board which is marked. The goal of the game is to move the pebble
to square number N - 1.

During each turn we throw a six-sided die, with numbers from 1 to 6 on its faces,
and consider the number K, which shows on the upper face after the die comes to
rest. Then we move the pebble standing on square number I to square number I + K,
providing that square number I + K exists. If square number I + K does not exist, we
throw the die again until we obtain a valid move. Finally, we mark square number
I + K.

After the game finishes (when the pebble is standing on square number N - 1), we
calculate the result. The result of the game is the sum of the numbers written on
all marked squares.

For example, given the following array:

    A[0] = 1
    A[1] = -2
    A[2] = 0
    A[3] = 9
    A[4] = -1
    A[5] = -2

one possible game could be as follows:
    - the pebble is on square number 0, which is marked;
    - we throw 3; the pebble moves from square number 0 to square number 3; we mark
      square number 3;
    - we throw 5; the pebble does not move, since there is no square number 8 on the
      board;
    - we throw 2; the pebble moves to square number 5; we mark this square and the
      game ends.

The marked squares are 0, 3 and 5, so the result of the game is 1 + 9 + (-2) = 8.
This is the maximal possible result that can be achieved on this board.

Write a function:

def solution(A)

that, given a non-empty array A of N integers, returns the maximal result that can
be achieved on the board represented by array A.

For example, given the array above, the function should return 8, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [2..100,000];
each element of array A is an integer within the range [-10,000..10,000].

Same shape as NeetCode's Min Cost Climbing Stairs: there you look back 2 steps and
take the min, here 6 squares and take the max.
"""

def solution(A):
    # dp[i] = maximal result when the pebble lands on square i
    # one throw (1..6) reaches i from any of the 6 squares before it,
    # so take the max of those and add the number on square i
    n = len(A)
    dp = [0] * n
    dp[0] = A[0]                        # start square is always marked

    for i in range(1, n):
        # ⚠️ max(0, i-6): near the start there are fewer than 6 squares behind
        max_before = max(dp[max(0, i-6):i])
        dp[i] = A[i] + max_before

    return dp[n-1]                      # ⚠️ must END on the last square: dp[n-1], not max(dp)

# DRY RUN: A = [1, -2, 0, 9, -1, -2]
#   i=1: max_before = max(1)            = 1   -> dp[1] = -2 + 1  = -1
#   i=2: max_before = max(1, -1)        = 1   -> dp[2] =  0 + 1  =  1
#   i=3: max_before = max(1, -1, 1)     = 1   -> dp[3] =  9 + 1  = 10
#   i=4: max_before = max(1, -1, 1, 10) = 10  -> dp[4] = -1 + 10 =  9
#   i=5: max_before = max(.., 10, 9)    = 10  -> dp[5] = -2 + 10 =  8
#   dp = [1, -1, 1, 10, 9, 8]  -> 8  (path 0 -> 3 -> 5)
#
# Time: O(6N) = O(N), Space: O(N)
