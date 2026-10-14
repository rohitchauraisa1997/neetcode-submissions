"""
Valid Parentheses (NeetCode)
============================

You are given a string s consisting of the following characters: '(', ')',
'{', '}', '[' and ']'.

The input string s is valid if and only if:
    1. Every open bracket is closed by the same type of close bracket.
    2. Open brackets are closed in the correct order.
    3. Every close bracket has a corresponding open bracket of the same type.

Return true if s is a valid string, and false otherwise.

Example 1:
    Input:  s = "[]"
    Output: true

Example 2:
    Input:  s = "([{}])"
    Output: true

Example 3:
    Input:  s = "[(])"
    Output: false
    Explanation: The brackets are not closed in the correct order.

Constraints:
    1 <= s.length <= 1000
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        # for strings like "["
        if len(s)%2!=0:
            return False

        for char in s:
            if char in "([{":
                stack.append(char)
            elif char in "}])":
                if len(stack) > 0:
                    # for strings like "]]"
                    popped = stack.pop()
                    popped_char_string_pair = popped+char
                    if popped_char_string_pair not in ["()", "{}", "[]"] :
                        return False
                else:
                    return False
            else:
                None

        return len(stack)==0