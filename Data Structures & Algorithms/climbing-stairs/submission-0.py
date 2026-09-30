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

def fib_iterative(n: int) -> int:
    # Bottom-up with a 2-value sliding window: a = F(i), b = F(i+1)
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a
    # Time: O(n), Space: O(1)