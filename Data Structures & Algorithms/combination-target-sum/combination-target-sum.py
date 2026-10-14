r"""
Combination Target Sum (NeetCode)
=================================

You are given an array of distinct integers nums and a target integer target.
Your task is to return a list of all unique combinations of nums where the
chosen numbers sum to target.

The same number may be chosen from nums an unlimited number of times. Two
combinations are the same if the frequency of each of the chosen numbers is
the same, otherwise they are different.

You may return the combinations in any order and the order of the numbers in
each combination can be in any order.

Example 1:
    Input:  nums = [2,5,6,9], target = 9
    Output: [[2,2,5],[9]]
    Explanation:
    2 + 2 + 5 = 9. We use 2 twice, and 5 once.
    9 = 9. We use 9 once.

Example 2:
    Input:  nums = [3,4,5], target = 16
    Output: [[3,3,3,3,4],[3,3,5,5],[4,4,4,4],[3,4,4,5]]

Example 3:
    Input:  nums = [3], target = 5
    Output: []

Constraints:
    All elements of nums are distinct.
    1 <= nums.length <= 20
    2 <= nums[i] <= 30
    2 <= target <= 30

Explanation (decision tree for nums = [2,3,6,7], target = 7):

    At every node there are two choices for nums[i]:
      +n     = include nums[i] and STAY at i  (it can be used again)
      skip n = never use nums[i] again, move to i+1

                                 []
                  +2 /                          \ skip 2
                   [2]                           []
          +2 /             \ skip 2     +3 /           \ skip 3
         [2,2]            [2]           [3]             []
    +2 /     \ skip 2  +3 /   \ skip 3   X        +6 /     \ skip 6
  [2,2,2]    [2,2]    [2,3]     [2]               [6]        []
     X    +3 /  \ skip  X        X                 X   +7 /   \ skip 7
        [2,2,3]  [2,2]                                 [7]     []
         = 7       X                                   = 7     end
        FOUND                                         FOUND

    X = every path below goes over 7 (or runs out of numbers), so it's cut off

    Answer: [[2,2,3], [7]]

    Why no duplicates like [3,2,2]: once you go down "skip 2", 2 is gone for
    that whole subtree. So every combination is built in the order of nums,
    and each one is found exactly once.

    Why stop at total > target: nums are all positive, so adding more can
    only make the total bigger. That branch can never come back to 7.

    In the code:
      - "+n" branch    = subsets.append(nums[index]); dfs(index, total + nums[index])
      - "skip n" branch = subsets.pop();               dfs(index + 1, total)
      - FOUND          = total == target -> record a copy of subsets
      - X              = total > target or index past the end -> return
"""

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