"""
Replace Elements With Greatest Element On Right Side (NeetCode)
===============================================================

You are given an array arr, replace every element in that array with the
greatest element among the elements to its right, and replace the last element
with -1.

After doing so, return the array.

Example 1:
    Input:  arr = [2,4,5,3,1,2]
    Output: [5,5,3,2,2,-1]

Example 2:
    Input:  arr = [3,3]
    Output: [3,-1]

Constraints:
    1 <= arr.length <= 10,000
    1 <= arr[i] <= 100,000
"""

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # traverse right-to-left,
        # tracking the max of everything seen so far

        max_right = -1

        for i in range(len(arr)-1, -1, -1):
            # stage the next max BEFORE overwriting arr[i],
            # otherwise we lose arr[i]'s original value
            new_max = max(max_right, arr[i])
            arr[i] = max_right
            max_right = new_max

        return arr