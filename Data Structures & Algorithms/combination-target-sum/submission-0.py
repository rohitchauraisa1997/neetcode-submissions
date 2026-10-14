class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        subsets = []                # current combination, shared by all calls

        def dfs(index, total):
            # ⚠️ goal check before bounds, or a combo ending on the last index is lost
            if total==target:
                return result.append(subsets[:])    # ⚠️ copy, subsets keeps changing

            # out of numbers, or overshot (nums are positive, so total only grows)
            if index >= len(nums) or total > target:
                return

            # CHOOSE nums[index]; ⚠️ stay at index since reuse is allowed
            subsets.append(nums[index])
            dfs(index, total+nums[index])

            # UN-CHOOSE, then skip nums[index] for good
            subsets.pop()
            dfs(index+1, total)     # ⚠️ total, not total+nums[index]: it was popped

        dfs(0,0)
        return result

# Time: O(2^(target/min(nums))), Space: O(target/min(nums))