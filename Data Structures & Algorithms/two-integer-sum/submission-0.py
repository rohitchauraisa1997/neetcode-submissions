class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index_map = {}
        for idx, num in enumerate(nums):
            num_index_map[num] = idx
        
        for idx, num in enumerate(nums):
            diff = target - num

            if diff in num_index_map and num_index_map[diff]!=idx:
                return [idx,num_index_map[diff]]
        
        return []