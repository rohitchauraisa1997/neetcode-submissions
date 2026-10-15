"""
Count Number of Islands (NeetCode) -- another approach (BFS)
Problem statement: see count-number-of-islands-dfs.py
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        nRows, nCols = len(grid), len(grid[0])
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        islands = 0
        visit = set()                   # cells already part of a counted island

        # once we find a single 1, bfs spreads level by level to all the land
        # connected to it and adds the whole island to visit
        def bfs(r,c):
            q = deque()
            q.append((r,c))
            visit.add((r,c))            # ⚠️ mark the start too, not just neighbours

            while q:
                row, col = q.popleft()  # popleft = BFS (pop() would make it DFS)
                for dr, dc in directions:
                    newRow, newCol = row+dr, col+dc
                    # skip: off the grid, water, or already visited
                    if (newRow<0 or newCol<0 or
                        newRow==nRows or newCol==nCols or
                        grid[newRow][newCol] == "0" or
                        (newRow, newCol) in visit):
                        continue
                    q.append((newRow, newCol))
                    visit.add((newRow, newCol))   # ⚠️ mark on push, so it's queued only once

        for r in range(nRows):
            for c in range(nCols):
                # ⚠️ check visit too, or every cell of an island starts a new count
                if grid[r][c]=="1" and (r,c) not in visit:
                    bfs(r,c)
                    islands += 1

        return islands

# Time: O(rows * cols), Space: O(rows * cols) for visit + queue