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