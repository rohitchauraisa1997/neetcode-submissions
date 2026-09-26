class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if op == "C":
                stack.pop()
            elif op == "D":
                last_el = stack[-1]
                doubled = 2*last_el
                stack.append(doubled)
            elif op == "+":
                new_el = stack[-1]+stack[-2]
                stack.append(new_el)
            else:
                stack.append(int(op))

        return sum(stack)