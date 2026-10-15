"""
Max Consecutive Ones (NeetCode)
===============================

Given a binary array nums, return the maximum number of consecutive 1's in the
array.

Example 1:
    Input:  nums = [1,1,0,1,1,1]
    Output: 3

Example 2:
    Input:  nums = [1,0,1,1,0,1]
    Output: 2

Constraints:
    1 <= nums.length <= 100,000
    nums[i] is either 0 or 1.
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        count = 0

        for num in nums:
            if num==1:
                count+=1
                max_count = max(max_count, count)
            else:
                count = 0
        
        return max_count
