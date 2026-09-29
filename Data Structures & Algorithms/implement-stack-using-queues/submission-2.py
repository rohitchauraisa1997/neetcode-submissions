class MyStack:
    # Stack using a single queue.
    # q holds the stack in order: front = top (newest).
    # push O(n), pop/top O(1)
    # Sim run (front on the left):
    #   op        after append   rotations                  q after
    #   push(1)   [1]            0                          [1]
    #   push(2)   [1, 2]         1: [2, 1]                  [2, 1]
    #   push(3)   [2, 1, 3]      2: [1, 3, 2] -> [3, 2, 1]  [3, 2, 1]
    #   pop()     returns 3, q = [2, 1]
    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)                         # new element goes to the back
        for i in range(len(self.q) - 1):         # rotate the old elements (all but x)
            self.q.append(self.q.popleft())      # front -> back, until x is at the front

    def pop(self) -> int:
        return self.q.popleft()                  # front = newest

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0