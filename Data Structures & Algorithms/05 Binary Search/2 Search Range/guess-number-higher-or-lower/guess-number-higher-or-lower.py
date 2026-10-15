"""
Guess Number Higher or Lower (NeetCode)
=======================================

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is
higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible
results:
    -1: Your guess is higher than the number I picked (i.e. num > pick).
     1: Your guess is lower than the number I picked (i.e. num < pick).
     0: Your guess is equal to the number I picked (i.e. num == pick).

Return the number that I picked.

Example 1:
    Input:  n = 5, pick = 3
    Output: 3

Example 2:
    Input:  n = 15, pick = 10
    Output: 10

Example 3:
    Input:  n = 1, pick = 1
    Output: 1

Constraints:
    1 <= n <= ((2^31) - 1)
    1 <= pick <= n
"""

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # Classic binary search over the range 1..n
        l = 1
        r = n

        while l <= r:
            mid = (l + r) // 2
            res = guess(mid)       # ⚠️ API returns result relative to YOUR guess

            if res == 1:           # picked > mid → my guess too low → go right
                l = mid + 1
            elif res == -1:        # picked < mid → my guess too high → go left
                r = mid - 1
            else:                  # res == 0 → correct guess
                return mid

        return 0  # unreachable: picked number is guaranteed in 1..n