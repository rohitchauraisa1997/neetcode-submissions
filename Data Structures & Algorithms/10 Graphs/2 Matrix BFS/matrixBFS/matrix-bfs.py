"""
Matrix Breadth-First Search: Shortest Path (NeetCode)
=====================================================

You are given a binary matrix grid where 0s represent land and 1s represent
rocks that can not be traversed.

Return the length of the shortest path from the top-left corner of grid to the
bottom-right corner such that all traversed cells are land cells. You may only
move vertically or horizontally through land cells.

Note:
    - If there is no such path, return -1.
    - The length of a path is the number of MOVES from the starting cell to the
      ending cell.

Example 1:
    Input: grid = [
        [0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 0]
      ]
    Output: 6

Explanation:

    Only BFS gives the shortest path here: it reaches cells in order of
    distance, so the first time the target is popped is the shortest way there.
    Process the queue one LEVEL at a time (snapshot len(queue)); every cell in
    a level is the same number of moves from the start.

      level 0: (0,0)                       length 0
      level 1: (0,1)                       length 1
      level 2: (0,2)                       length 2
      ...      each level is one move further, target popped at length 6

    Compare: Shortest Path in Binary Matrix counts CELLS and allows diagonals.
"""

class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        nRows, nCols = len(grid), len(grid[0])
        # ⚠️ start on a rock -> no path at all
        if grid[0][0] == 1:
            return -1

        # BFS goes level by level: every cell in the queue right now is `length`
        # moves from the start, so the first time we pop the target, that's the
        # shortest path
        def bfs(r,c):
            queue = deque()
            visit = set()
            directions = [(0,1),(1,0),(0,-1),(-1,0)]
            length = 0                     # moves taken to reach the current level
            queue.append((r,c))
            visit.add((r,c))

            while len(queue)>0:
                # ⚠️ snapshot the level size; cells appended below belong to the next level
                for _ in range(len(queue)):
                    row, col = queue.popleft()
                    if (row,col) == (nRows-1, nCols-1):
                        return length      # covers a 1x1 grid too: 0 moves

                    for dr, dc in directions:
                        newRow, newCol = row+dr, col+dc
                        # skip: off the grid, rock, or already queued
                        if (newRow<0 or newRow==nRows or
                            newCol<0 or newCol==nCols or
                            grid[newRow][newCol]==1 or
                            (newRow, newCol) in visit):
                            continue

                        queue.append((newRow, newCol))
                        visit.add((newRow, newCol))   # mark on push, so it's queued once
                        
                # once the for loop is finished meaning one level is finished.
                length += 1                # ⚠️ once per LEVEL (after the for), not per cell

            return -1                   # ⚠️ queue emptied, target unreachable

        return bfs(0,0)

# Time: O(rows * cols), Space: O(rows * cols)