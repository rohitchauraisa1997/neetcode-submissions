"""
Valid Anagram (NeetCode)
========================

Given two strings s and t, return true if the two strings are anagrams of each
other, otherwise return false.

An anagram is a string that contains the exact same characters as another
string, but the order of the characters can be different.

Example 1:
    Input:  s = "racecar", t = "carrace"
    Output: true

Example 2:
    Input:  s = "jar", t = "jam"
    Output: false

Constraints:
    s and t consist of lowercase English letters.

Shorter alternatives: `Counter(s) == Counter(t)` (O(n)) or
`sorted(s) == sorted(t)` (O(n log n)).
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # count every char in s, then "spend" those counts on t
        charMap = {}

        for char in s:
            if char in charMap:
                charMap[char] += 1
            else:
                charMap[char] = 1

        for char in t:
            # t uses a char s doesn't have, or more of it than s has
            if char in charMap and charMap[char]>0:
                charMap[char] -= 1
            else:
                return False

        # ⚠️ leftover counts = s had chars t never used (t is shorter),
        #    e.g. s = "aab", t = "ab" passes the loop above but isn't an anagram
        for char in charMap:
            if charMap[char]>0:
                return False

        return True

    # Time: O(n), Space: O(k) for k distinct chars (at most 26 for lowercase)

    def isAnagram2(self, s: str, t: str) -> bool:
        # different lengths can never be anagrams: cheap early exit
        if len(s) != len(t):
            return False

        # count both strings in one pass (same length, so one index works for both)
        countS, countT = {}, {}

        for i in range(len(s)):
            # .get(key, 0): 0 the first time a char is seen, no if/else needed
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        # dicts are equal when they have the same keys with the same counts
        return countS == countT

    # Time: O(n), Space: O(k)