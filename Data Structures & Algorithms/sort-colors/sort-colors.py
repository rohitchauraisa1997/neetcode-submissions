"""
Sort Colors (NeetCode)
======================

You are given an array nums consisting of n elements where each element is an
integer representing a color:
    - 0 represents red
    - 1 represents white
    - 2 represents blue

Your task is to sort the array in-place such that elements of the same color
are grouped together and arranged in the order: red (0), white (1), and then
blue (2).

You must not use any built-in sorting functions to solve this problem.

Example 1:
    Input:  nums = [1,0,1,2]
    Output: [0,1,1,2]

Example 2:
    Input:  nums = [2,1,0]
    Output: [0,1,2]

Constraints:
    1 <= nums.length <= 300.
    0 <= nums[i] <= 2.

Follow up: Could you come up with a one-pass algorithm using only constant
extra space?
"""

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Counting sort: values are only 0, 1, 2 → count each
        counter = [0] * 3   # counter[v] = how many times v appears

        # Pass 1: count occurrences
        for num in nums:
            counter[num] += 1   # value doubles as index

        # Pass 2: overwrite nums in order 0s → 1s → 2s
        index = 0               # next write position in nums
        for i in range(3):
            while counter[i] > 0:
                nums[index] = i
                index += 1
                counter[i] -= 1