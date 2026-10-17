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