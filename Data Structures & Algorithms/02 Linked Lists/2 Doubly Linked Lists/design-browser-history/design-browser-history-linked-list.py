"""
Design Browser History (NeetCode) -- another approach
Problem statement: see design-browser-history-array.py
"""

class Node:
    def __init__(self,val):
        self.val = val
        self.prev = None
        self.next = None

class BrowserHistory:

    def __init__(self, homepage: str):
        # keeps track of the latest page we r on
        self.curr = Node(homepage)        

    def visit(self, url: str) -> None:
        new_node = Node(url)
        new_node.prev = self.curr
        self.curr.next = new_node
        self.curr = new_node

    def back(self, steps: int) -> str:
        # We check self.curr.prev (not self.curr) so we never
        # move onto None -- self.curr stays a valid node.
        while self.curr.prev and steps>0:
            steps -= 1
            self.curr = self.curr.prev
        return self.curr.val

    def forward(self, steps: int) -> str:
        # Same idea, forward direction. Guard on self.curr.next so
        # we never step past the newest page into None.
        while  self.curr.next and steps>0:
            steps -= 1
            self.curr = self.curr.next
        return self.curr.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)