"""
Design Browser History (NeetCode)
=================================

You have a browser of one tab where you start on the homepage and you can visit
another url, get back in the history number of steps or move forward in the
history number of steps.

Implement the BrowserHistory class:
    - BrowserHistory(string homepage) Initializes the object with the homepage
      of the browser.
    - void visit(string url) Visits url from the current page. It clears up all
      the forward history.
    - string back(int steps) Move steps back in history. If you can only return
      x steps in the history and steps > x, you will return only x steps.
      Return the current url after moving back in history at most steps.
    - string forward(int steps) Move steps forward in history. If you can only
      forward x steps in the history and steps > x, you will forward only x
      steps. Return the current url after forwarding in history at most steps.

Example 1:
    Input:
    ["BrowserHistory", "visit", "visit", "visit", "back", "back", "forward",
     "visit", "forward", "back", "back"]
    [["neetcode.io"], ["google.com"], ["facebook.com"], ["youtube.com"], [1],
     [1], [1], ["linkedin.com"], [2], [2], [7]]

    Output:
    [null, null, null, null, "facebook.com", "google.com", "facebook.com",
     null, "linkedin.com", "google.com", "neetcode.io"]

    Explanation:
    BrowserHistory browserHistory = new BrowserHistory("neetcode.io");
    browserHistory.visit("google.com");   // neetcode.io -> google.com
    browserHistory.visit("facebook.com"); // google.com -> facebook.com
    browserHistory.visit("youtube.com");  // facebook.com -> youtube.com
    browserHistory.back(1);    // back to facebook.com, return "facebook.com"
    browserHistory.back(1);    // back to google.com, return "google.com"
    browserHistory.forward(1); // forward to facebook.com, return "facebook.com"
    browserHistory.visit("linkedin.com"); // facebook.com -> linkedin.com
    browserHistory.forward(2); // can't move forward, return "linkedin.com"
    browserHistory.back(2);    // back two steps to google.com, return it
    browserHistory.back(7);    // can only go back one step, return "neetcode.io"

Constraints:
    1 <= homepage.length <= 20
    1 <= url.length <= 20
    1 <= steps <= 100
    homepage and url consist of '.' or lower case English letters.
    At most 5000 calls will be made to visit, back, and forward.
"""

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