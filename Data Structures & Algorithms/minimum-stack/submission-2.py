class MinStack:

    def __init__(self):
        # whole logic is to have two stacks for O(1) time complexity.
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_stack)>0:
            # min_stack[i] holds the min of stack[0..i], so the top of
            # min_stack is always the current global minimum.
            self.min_stack.append(min(val, self.min_stack[-1]))
        else:
            self.min_stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]