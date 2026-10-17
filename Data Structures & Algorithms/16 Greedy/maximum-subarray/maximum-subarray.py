"""
Maximum Subarray (NeetCode)
===========================

Given an array of integers nums, find the subarray with the largest sum and
return the sum.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
    Input:  nums = [2,-3,4,-2,2,1,-1,4]
    Output: 8
    Explanation: The subarray [4,-2,2,1,-1,4] has the largest sum 8.

Example 2:
    Input:  nums = [-1]
    Output: -1

Constraints:
    1 <= nums.length <= 1000
    -1000 <= nums[i] <= 1000

Same problem as Codility's MaxSliceSum (lesson 9, Maximum slice problem).
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's algorithm: one pass, tracking the best sum of a slice that ENDS at r
        # len of nums is >= 1
        currSum = 0                 # ⚠️ empty slice: the loop adds nums[0] itself
        maxSubSum = nums[0]         # ⚠️ not 0: if every number is negative, the answer is negative
        r = 0

        while r < len(nums):
            currSum += nums[r]                      # extend the current slice to include nums[r]
            maxSubSum = max(maxSubSum, currSum)     # ⚠️ record BEFORE resetting (all-negative case)

            # a +ve currSum before nums[r] helps it, so keep extending;
            # a -ve one only drags the next numbers down, so drop it
            # and start a fresh slice from the next index
            if currSum < 0:
                currSum = 0

            r += 1

        return maxSubSum

# Time: O(n), Space: O(1)