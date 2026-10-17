"""
Climbing Stairs (NeetCode)
==========================

You are given an integer n representing the number of steps to reach the top
of a staircase. You can climb with either 1 or 2 steps at a time.

Return the number of distinct ways to climb to the top of the staircase.

Example 1:
    Input:  n = 2
    Output: 2
    Explanation:
    1. 1 + 1 = 2
    2. 2 = 2

Example 2:
    Input:  n = 3
    Output: 3
    Explanation:
    1. 1 + 1 + 1 = 3
    2. 1 + 2 = 3
    3. 2 + 1 = 3

Constraints:
    1 <= n <= 30
"""

# ---------------------------------------------------------------------------
# PROBLEM: Climbing Stairs (LeetCode 70)
# n steps to the top; each move is 1 or 2 steps. Count distinct ways.
#
# STAIRCASE (n = 5), start on the ground at step 0:
#
#                          2-step       ___
#                        .------.  ___|   |
#                   ___ /       v|   |   |
#              ___|   |  1-step |   |   |
#         ___|   |   | ------> |   |   |
#   o    |   |   |   |         |   |   |
#  /|\___|___|___|___|_________|___|___|
#    0    1    2    3          4    5
#
# DECISION TREE (brute force = O(2^n)):
#   From each step, branch to +1 or +2. Overshooting past 5 (e.g. 6) = dead end.
#
#                    0
#                 /     \
#                1       2        <- subtree "2" appears again under 1
#              /   \    / \
#             2     3  3   4      <- repeated subtrees (3, 4, ...)
#            / \   ...
#           3   4
#          / \   \
#         4   5   5 ...
#        / \
#       5   6x
#
#   Each step's answer depends only on the two steps below it
#   -> solve each step once = O(n).
#
# DP TABLE (filled left -> right):
#   dp[i] = ways to reach step i from step 0
#
#   step:  0   1   2   3   4   5
#   dp  :  -   1   2   3   5   8      dp[i] = dp[i-1] + dp[i-2]
#                              ^ answer
#
#   ways(i) = fib(i+1)  -> same sequence as Fibonacci, offset by one index
#
#   i       :  0  1  2  3  4  5  6
#   fib(i)  :  0  1  1  2  3  5  8
#   ways(i) :  1  1  2  3  5  8  13
#
#   Same recurrence, only the starting values differ (fib: 0,1 | stairs: 1,1).
# ---------------------------------------------------------------------------

class Solution:
    def climbStairs(self, n: int) -> int:
        # Bottom-up DP (tabulation)
        # ways(i) = ways(i-1) + ways(i-2): last move was a 1-step or a 2-step
        if n<=2:
            return n            # 1 -> {1}, 2 -> {1+1, 2}

        dp = [0]*(n+1)          # n+1 so dp[n] exists; dp[0] unused
        dp[1] = 1
        dp[2] = 2

        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]            # Time: O(N), Space: O(N)

    def climbStairs_O1(self, n: int) -> int:
        # Only the last two values are ever needed -> sliding window, like fib
        one, two = 1, 1         # one = ways(i-1), two = ways(i-2)
        for _ in range(n - 1):
            one, two = one + two, one
        return one              # Time: O(N), Space: O(1)


# ---------------------------------------------------------------------------
# FIBONACCI: F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2)
#   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# ---------------------------------------------------------------------------

def fib_recursive(n: int) -> int:
    # Plain recursion: recomputes the same subproblems (same tree as above)
    if n <= 1:
        return n                # F(0) = 0, F(1) = 1
    return fib_recursive(n-1) + fib_recursive(n-2)
    # Time: O(2^n), Space: O(n) call stack

def fib_memo(n: int, memo=None) -> int:
    # Top-down DP (memoization): same recursion, cache each F(k) once
    # memo=None, not memo={}: a mutable default would persist across calls
    if memo is None:
        memo = {}
    if n <= 1:
        return n
    if n in memo:
        return memo[n]
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]
    # Time: O(n), Space: O(n) cache + call stack

def fib_dp_table(n: int) -> int:
    # Bottom-up DP (tabulation), FULL table: the whole picture.
    # dp[i] = F(i); fill left -> right, each from the two before it.
    if n < 2:
        return n
    dp = [0] * (n + 1)          # n+1 slots so dp[n] exists
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
    # n = 5:  i   : 0  1  2  3  4  5
    #         dp  : 0  1  1  2  3  5   -> dp[5] = 5
    # Time: O(n), Space: O(n) for the table

def fib_dp_two_slots(n: int) -> int:
    # Same table, but only the last two cells are ever read, so keep just those:
    # dp[0] = F(i-2), dp[1] = F(i-1)  (a sliding window of size 2 over the table)
    if n < 2:
        return n
    dp = [0, 1]
    i = 2
    while i <= n:
        tmp = dp[1]             # ⚠️ save F(i-1) before overwriting dp[1]
        dp[1] = dp[0] + dp[1]   # new F(i)
        dp[0] = tmp             # slide: old F(i-1) becomes the "two back" value
        i += 1
    return dp[1]
    # n = 5:   i=2: [0,1] -> [1,1]
    #          i=3: [1,1] -> [1,2]
    #          i=4: [1,2] -> [2,3]
    #          i=5: [2,3] -> [3,5]   -> dp[1] = 5
    # fib_dp_two_slots(10) = 55
    # Time: O(n), Space: O(1)

# fib_iterative below is the same window again, with two variables (a, b)
# instead of a 2-slot list, and the swap done in one line.

def fib_iterative(n: int) -> int:
    # Bottom-up with a 2-value sliding window: a = F(i), b = F(i+1)
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a
    # Time: O(n), Space: O(1)