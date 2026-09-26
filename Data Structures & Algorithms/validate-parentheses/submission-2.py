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