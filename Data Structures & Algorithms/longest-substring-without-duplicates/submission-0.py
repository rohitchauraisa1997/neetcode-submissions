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