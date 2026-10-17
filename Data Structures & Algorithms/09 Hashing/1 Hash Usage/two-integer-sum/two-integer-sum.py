"""
Two Integer Sum (NeetCode)
==========================

Given an array of integers nums and an integer target, return the indices i and
j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that
satisfy the condition.

Return the answer with the smaller index first.

Example 1:
    Input:  nums = [3,4,5,6], target = 7
    Output: [0,1]
    Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

Example 2:
    Input:  nums = [4,5,6], target = 10
    Output: [0,2]

Example 3:
    Input:  nums = [5,5], target = 10
    Output: [0,1]

Constraints:
    2 <= nums.length <= 1000
    -10,000,000 <= nums[i] <= 10,000,000
    -10,000,000 <= target <= 10,000,000
    Only one valid answer exists.
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # value -> index for every number seen SO FAR (only to the left of `index`)
        nums_index_map = {}

        for index, num in enumerate(nums):
            diff = target-num           # the partner this number needs
            # partner already seen? it's to the left, so its index is the smaller one
            if diff in nums_index_map:
                return [nums_index_map[diff], index]
            # ⚠️ store AFTER the check: checking first means a number can't pair
            #    with itself (target 6, num 3 alone isn't an answer), yet a second
            #    3 later still finds the first one ([3,3] -> [0,1])
            nums_index_map[num] = index

        # (the problem guarantees exactly one answer, so the loop always returns)

# Time: O(n), one pass, each lookup O(1). Space: O(n) for the map