"""
Concatenation of Array (NeetCode) -- another approach
Problem statement: see concatenation-of-array-append.py
"""

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        new_nums = [0]*2*nums_len

        for i in range(nums_len):
            new_nums[i] = nums[i]
            new_nums[i+nums_len] = nums[i]
        
        return new_nums