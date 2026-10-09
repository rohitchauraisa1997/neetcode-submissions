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