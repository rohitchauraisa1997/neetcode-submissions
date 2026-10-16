"""
Max Area of Island (NeetCode)
=============================

You are given a matrix grid where grid[i] is either a 0 (representing water)
or 1 (representing land).

An island is defined as a group of 1's connected horizontally or vertically.
You may assume all four edges of the grid are surrounded by water.

The area of an island is defined as the number of cells within the island.

Return the maximum area of an island in grid. If no island exists, return 0.

Example 1:
    Input: grid = [
        [0,1,1,0,1],
        [1,0,1,0,1],
        [0,1,1,0,1],
        [0,1,0,0,1]
      ]
    Output: 6
    Explanation: 1's cannot be connected diagonally, so the maximum area of
    the island is 6.

Constraints:
    1 <= grid.length, grid[i].length <= 50

Explanation:

    Same search as Count Number of Islands, two differences:
      - the search RETURNS a size: 1 for this cell + the sizes found in all
        4 directions (DFS), or +1 for every cell pushed (BFS)
      - keep the max size instead of adding 1 per island

    ⚠️ grid holds ints (0/1) here, not strings ("0"/"1") like Number of Islands.
"""

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        nRows, nCols = len(grid), len(grid[0])
        visit = set()               # cells already part of a measured island
        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        # returns the size of the island containing (r,c), and marks all of it,
        # so no cell is counted twice
        def dfs(r,c):
            if r<0 or r==nRows or c<0 or c==nCols or grid[r][c]==0 or (r,c)in visit:
                return 0

            visit.add((r,c))

            area = 1                # this cell
            # ⚠️ add up ALL 4 directions; a return inside the loop only goes right
            for dr, dc in directions:
                area += dfs(r+dr, c+dc)
            return area

        area = 0
        for r in range(nRows):
            for c in range(nCols):
                # water and visited cells return 0, so calling dfs everywhere is safe
                area = max(area, dfs(r,c))

        return area

# Time: O(rows * cols), Space: O(rows * cols) for visit + recursion