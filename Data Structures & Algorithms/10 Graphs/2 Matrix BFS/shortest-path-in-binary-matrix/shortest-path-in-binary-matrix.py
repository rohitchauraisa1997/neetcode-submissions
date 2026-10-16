"""
Shortest Path in Binary Matrix (NeetCode)
=========================================

You are given an n x n binary matrix grid, return the length of the shortest
clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0))
to the bottom-right cell (i.e., (n - 1, n - 1)) such that:
    - All the visited cells of the path are 0.
    - All the adjacent cells of the path are 8-directionally connected (i.e.,
      they are different and they share an edge or a corner).

The length of a clear path is the number of visited cells of this path.

Example 1:
    Input: grid = [
        [0,1,0],
        [1,0,0],
        [1,1,0]
      ]
    Output: 3
    Explanation: (0,0) -> (1,1) -> (2,2), diagonal moves, 3 cells.

Example 2:
    Input: grid = [
        [1,0],
        [1,1]
      ]
    Output: -1

Constraints:
    n == grid.length
    n == grid[i].length
    1 <= n <= 100
    grid[i][j] is 0 or 1

Explanation:

    Same level-by-level BFS as the Matrix BFS lesson, two differences:
      - 8 directions (diagonals count as one step)
      - length counts CELLS, not moves, so it starts at 1 (a 1x1 grid -> 1)
"""

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        nRows, nCols = len(grid), len(grid[0])
        # ⚠️ start on a blocked cell -> no path
        if grid[0][0] == 1:
            return -1

        # BFS level by level: the first time we pop the bottom-right cell, that's the
        # shortest path. 8 directions here (diagonals allowed), unlike the matrix BFS lesson
        def bfs(r,c):
            directions = [(1,0),(1,1),(0,1),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
            queue = deque()
            visit = set()

            queue.append((r,c))
            visit.add((r,c))

            length = 1                  # ⚠️ counts CELLS on the path, so the start is 1

            while len(queue)>0:
                for _ in range(len(queue)):     # one full level per pass
                    row, col = queue.popleft()
                    if (row,col) == (nRows-1, nCols-1):
                        return length

                    for dr, dc in directions:
                        newRow, newCol = row+dr, col+dc
                        # skip: off the grid, blocked, or already queued
                        # ⚠️ check the NEIGHBOUR in visit, not the popped cell
                        if (newRow < 0 or newRow==nRows or
                            newCol < 0 or newCol==nCols or
                            grid[newRow][newCol]==1 or
                            (newRow, newCol) in visit):
                            continue

                        queue.append((newRow, newCol))
                        visit.add((newRow, newCol))   # mark on push, so it's queued once

                # once for is exited that means one level is traversed.
                length += 1             # ⚠️ once per LEVEL, after the for, not per cell

            return -1                   # target unreachable (or blocked)

        return bfs(0,0)

# Time: O(n^2), Space: O(n^2) for an n x n grid