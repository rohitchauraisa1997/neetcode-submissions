r"""
Subsets (NeetCode)
==================

Given an array nums of unique integers, return all possible subsets of nums.

The solution set must not contain duplicate subsets. You may return the
solution in any order.

Example 1:
    Input:  nums = [1,2,3]
    Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
    Input:  nums = [7]
    Output: [[],[7]]

Constraints:
    1 <= nums.length <= 10
    -10 <= nums[i] <= 10

Explanation (decision tree for nums = [1,2,3]):

    Screenshot: subsets-include-exclude.png (in this folder)

    Each level decides ONE element: include it (+n) or skip it.

                               []
                +1 /                         \ skip 1
                [1]                           []
         +2 /         \ skip         +2 /          \ skip
        [1,2]          [1]            [2]             []
    +3 /    \ skip  +3 /  \ skip   +3 /  \ skip   +3 /  \ skip
  [1,2,3]  [1,2]   [1,3]   [1]   [2,3]   [2]     [3]     []

    Nodes per level: 1 -> 2 -> 4 -> 8. Every level doubles, so n elements
    give 2^n leaves, and every leaf is one subset (including []).

    In the code:
      - left branch  = subsets.append(nums[index]); dfs(index+1)
      - right branch = subsets.pop();               dfs(index+1)
      - a leaf       = index == len(nums) -> record a copy of subsets
"""

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