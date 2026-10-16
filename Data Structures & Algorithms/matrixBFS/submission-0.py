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