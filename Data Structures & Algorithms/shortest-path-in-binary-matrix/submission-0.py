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