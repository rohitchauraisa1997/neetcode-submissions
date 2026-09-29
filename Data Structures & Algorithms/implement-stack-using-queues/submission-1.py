class MyStack:
    # ** MAIN OP ON PUSH **
    # Stack using two queues.
    # q1 always holds the stack in order: front = top (newest).
    # q2 is empty between calls; it's only a temp during push.
    # push O(n), pop/top O(1)
    # The idea is to use two queues: when pushing a new element, 
    # we add it to the empty second queue, then move all elements 
    # from the first queue behind it. This places the newest element 
    # at the front, ready to be popped first.
    
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q2.append(x)                        # new element goes first into empty q2
        while self.q1:                           # move old elements behind it
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1      # q2 becomes the main queue, q1 empty again

    def pop(self) -> int:
        return self.q1.popleft()                 # front = newest

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        return len(self.q1) == 0