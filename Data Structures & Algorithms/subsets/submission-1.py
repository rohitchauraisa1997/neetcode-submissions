class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.backtrack(nums, 0, [], res)
        return res

    def backtrack(self, nums, start, path, res):
        res.append(path[:])                 # every node is a subset; ⚠️ copy

        for j in range(start, len(nums)):
            path.append(nums[j])            # CHOOSE
            self.backtrack(nums, j + 1, path, res)   # EXPLORE (⚠️ j + 1, not start + 1)
            path.pop()                      # UN-CHOOSE