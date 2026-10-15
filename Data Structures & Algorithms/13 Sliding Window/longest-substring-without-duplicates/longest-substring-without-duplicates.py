"""
Longest Substring Without Repeating Characters (NeetCode)
=========================================================

Given a string s, find the length of the longest substring without duplicate
characters.

A substring is a contiguous sequence of characters within a string.

Example 1:
    Input:  s = "zxyzxyz"
    Output: 3
    Explanation: The string "xyz" is the longest without duplicate characters.

Example 2:
    Input:  s = "xxxx"
    Output: 1

Constraints:
    0 <= s.length <= 1000
    s may consist of printable ASCII characters.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding window: keep s[l..r] free of repeats. O(N).
        charSet = set()        # chars in the current window

        l = 0
        r = 0                  # redundant: the for loop sets r
        res = 0

        for r in range(len(s)):            # r drives the loop; l only moves in the while
            while s[r] in charSet:         # check the NEW char (r)
                charSet.remove(s[l])       # shrink from the left until the dup is gone
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)      # window length; CountDistinctSlices(similar codility question) uses += here res += r-l+1

        return res