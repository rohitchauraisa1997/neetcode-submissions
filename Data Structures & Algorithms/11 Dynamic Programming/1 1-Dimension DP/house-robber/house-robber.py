"""
House Robber (NeetCode)
=======================

You are given an integer array nums where nums[i] represents the amount of
money the ith house has. The houses are arranged in a straight line, i.e. the
ith house is the neighbor of the (i-1)th and (i+1)th house.

You are planning to rob money from the houses, but you cannot rob two adjacent
houses because the security system will automatically alert the police if two
adjacent houses were both broken into.

Return the maximum amount of money you can rob without alerting the police.

Example 1:
    Input:  nums = [1,1,3,3]
    Output: 4
    Explanation: nums[0] + nums[2] = 1 + 3 = 4.

Example 2:
    Input:  nums = [2,9,8,3,6]
    Output: 16
    Explanation: nums[0] + nums[2] + nums[4] = 2 + 8 + 6 = 16.

Constraints:
    1 <= nums.length <= 100
    0 <= nums[i] <= 100

Note: not simply "every other house": for [2,1,1,2] the best is the first and
last house (4), which skips two in a row. Taking the max of the two choices at
each house handles that.
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        # BOTTOM-UP DP (full table)
        # dp[i] = the most money you can take from houses 0..i
        #
        # At house i there are only two choices:
        #   skip house i -> you keep the best from houses 0..i-1    = dp[i-1]
        #   rob house i  -> house i-1 must be skipped (adjacent), so you add
        #                   nums[i] to the best from houses 0..i-2  = dp[i-2] + nums[i]
        # dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        if not nums:
            return 0
        # ⚠️ one house: dp[1] below would read nums[1], which doesn't exist
        if len(nums) == 1:
            return nums[0]

        dp = [0]*len(nums)
        dp[0] = nums[0]                     # one house: rob it
        dp[1] = max(nums[0], nums[1])       # two houses: they're adjacent, take the richer one

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1],            # skip house i
                        dp[i-2]+nums[i])    # rob house i

        return dp[len(nums)-1]              # best over all houses

    # nums = [2, 7, 9, 3, 1]
    #   i  :  0  1  2   3   4
    #   dp :  2  7  11  11  12     -> 12 (rob 2, 9, 1)
    # Time: O(n), Space: O(n)

    def rob2(self, nums: List[int]) -> int:
        # SAME DP, but dp[i] only ever reads dp[i-1] and dp[i-2],
        # so keep just those two values instead of the whole table
        best_two_back = 0       # dp[i-2]: best total up to two houses back
        best_one_back = 0       # dp[i-1]: best total up to the previous house

        for money in nums:
            # skip this house (keep best_one_back), or rob it (best_two_back + money)
            best_here = max(best_one_back, best_two_back + money)
            # slide the window forward by one house
            best_two_back = best_one_back
            best_one_back = best_here

        return best_one_back    # best total including the last house

    # Time: O(n), Space: O(1)