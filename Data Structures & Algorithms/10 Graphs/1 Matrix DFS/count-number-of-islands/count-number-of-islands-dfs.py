"""
Count Number of Islands (NeetCode)
==================================

Given a 2D grid grid where '1' represents land and '0' represents water, count
and return the number of islands.

An island is formed by connecting adjacent lands horizontally or vertically
and is surrounded by water. You may assume water is surrounding the grid
(i.e., all the edges are water).

Example 1:
    Input: grid = [
        ["0","1","1","1","0"],
        ["0","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
      ]
    Output: 1

Example 2:
    Input: grid = [
        ["1","1","0","0","1"],
        ["1","1","0","0","1"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
      ]
    Output: 4

Constraints:
    1 <= grid.length, grid[i].length <= 100
    grid[i][j] is '0' or '1'.

Explanation (what the search does):

    The outer loop finds an island by hitting any single 1. DFS/BFS then
    spreads to all the land connected to it and marks it, so the loop skips
    the rest of that island. Each island is counted exactly once.

      grid:      loop hits (0,0) -> marks the island -> islands = 1
      1 1 0 0    x x 0 0
      1 0 0 1    x 0 0 1     (0,1), (1,0) already marked: skipped
      0 0 1 1    0 0 1 1
                 loop hits (1,3) -> marks it + (2,2), (2,3) -> islands = 2

    Without the spreading step every 1 would count: 6 instead of 2.

    DFS (recursion) or BFS (queue) both work: this is reachability, so the
    order cells are visited in doesn't matter. See the Graphs cheatsheet.
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        nRows, nCols = len(grid), len(grid[0])
        visit = set()                       # cells already part of a counted island
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        islands = 0

        # once we find a single 1, dfs spreads to all the land connected to it
        # and adds the whole island to visit, so none of its cells get counted again
        def dfs(r,c):
            # stop: off the grid, already visited, or water
            if (r<0 or r==nRows or
                c<0 or c==nCols or
                (r,c) in visit or
                grid[r][c] == "0"):
                return

            visit.add((r,c))                # mark visited; grid stays unchanged
            # ALTERNATIVE (no visit set): sink the cell instead, a visited cell
            # becomes water, so the grid[r][c] == "0" check above stops on it
            # grid[r][c] = "0"              # ⚠️ changes the input grid
            for dr, dc in directions:       # spread to the whole island
                dfs(r+dr, c+dc)
            # ⚠️ no visit.remove(): reachability, not path counting

        for r in range(nRows):
            for c in range(nCols):
                # ⚠️ check visit too, or every cell of an island starts a new count
                # (with the grid alternative, grid[r][c]=="1" alone is enough)
                if grid[r][c]=="1" and (r,c) not in visit:
                    dfs(r,c)
                    islands+=1

        return islands

# Time: O(rows * cols)
# Space: O(rows * cols) for visit + recursion (grid alternative: recursion only)