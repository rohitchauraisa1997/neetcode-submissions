"""
Contains Duplicate (NeetCode)
=============================

Given an integer array nums, return true if any value appears more than once
in the array, otherwise return false.

Example 1:
    Input:  nums = [1, 2, 3, 3]
    Output: true

Example 2:
    Input:  nums = [1, 2, 3, 4]
    Output: false

Constraints:
    1 <= nums.length <= 10^5
    -10^9 <= nums[i] <= 10^9

Note: a set is enough here (only "seen or not" matters); a dict works too.
Returning as soon as a repeat appears avoids scanning the rest of the array.
"""

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_map = {}

        for num in nums:
            if num in nums_map:
                return True
            else:
                nums_map[num] = True

        return False