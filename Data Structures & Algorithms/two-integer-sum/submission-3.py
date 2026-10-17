class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_index_map = {}
        for index, num in enumerate(nums):
            diff = target-num
            if diff in nums_index_map:
                return [nums_index_map[diff], index]
            nums_index_map[num] = index
