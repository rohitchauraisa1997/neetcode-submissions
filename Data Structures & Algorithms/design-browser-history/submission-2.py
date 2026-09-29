class BrowserHistory:
    # Dynamic array + pointer.
    #   stack       : every page ever written; slots after self.len are dead forward history
    #   curr_index  : page we're currently on
    #   len         : index of the LAST VALID page (logical end), not len(stack)
    def __init__(self, homepage: str):
        self.stack = [homepage]
        self.curr_index = 0
        self.len = 0

    def visit(self, url: str) -> None:
        # Visiting always writes to curr_index + 1 and wipes all forward history.
        #
        # e.g. stack = [yt, fb, google, yahoo], curr = 3 (yahoo), len = 3
        #   back(2)          -> curr = 1 (fb)
        #   visit(crunchy)   -> curr = 2; slot 2 already exists, so overwrite it
        #                       stack = [yt, fb, crunchy, yahoo], len = 2
        #   yahoo is still physically in the array but is past len -> dead,
        #   so forward() can't reach it, and a later visit will overwrite it.
        #
        # Overwriting dead slots instead of slicing the list (stack[:curr+1])
        # keeps visit O(1) with no reallocation.
        self.curr_index += 1
        if self.curr_index < len(self.stack):   # physical slot exists -> reuse it
            self.stack[self.curr_index] = url
        else:                                   # at the physical end -> grow
            self.stack.append(url)
        self.len = self.curr_index              # new page is now the last valid one

    def back(self, steps: int) -> str:
        # clamp at 0: can't go before the homepage
        index = max(self.curr_index - steps, 0)
        self.curr_index = index
        return self.stack[index]

    def forward(self, steps: int) -> str:
        # clamp at self.len (logical end), **NOT len(stack)**: slots past len are dead
        index = min(self.curr_index + steps, self.len)
        self.curr_index = index
        return self.stack[index]