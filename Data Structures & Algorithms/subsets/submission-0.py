class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subsets = []                # current subset, shared by all calls

        def dfs(index):
            # decided include/exclude for every element -> one full subset
            if index>=len(nums):
                # ⚠️ copy: subsets keeps changing after this
                # ⚠️ append() returns None; works, but `append` then `return` is clearer
                return res.append(subsets[:])

            # CHOOSE: include nums[index], then EXPLORE
            subsets.append(nums[index])
            dfs(index+1)

            # UN-CHOOSE: ⚠️ pop before the exclude branch, or nums[index] leaks into it
            subsets.pop()
            dfs(index+1)            # EXPLORE without nums[index]

        dfs(0)
        return res

# Time: O(n * 2^n), Space: O(n)