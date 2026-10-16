class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        nRows, nCols = len(grid), len(grid[0])
        visit = set()               # cells already part of a measured island
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        area = 0

        # once we find a single 1, bfs spreads to all the land connected to it,
        # adds the whole island to visit, and returns its size
        def bfs(r,c):
            q = deque()
            q.append((r,c))
            visit.add((r,c))        # mark the start too, not just neighbours
            res = 1                 # the start cell counts as 1

            while q:
                row, col = q.popleft()      # popleft = BFS (pop() would make it DFS)
                for dr, dc in directions:
                    # ⚠️ neighbours of the POPPED cell (row, col), not the start (r, c)
                    newRow, newCol = row+dr, col+dc
                    # skip: off the grid, water (ints here, not "0"), or already visited
                    if (newRow<0 or newRow==nRows or 
                        newCol<0 or newCol==nCols or
                        grid[newRow][newCol]==0 or
                        (newRow, newCol) in visit
                        ):
                        continue
                    
                    q.append((newRow,newCol))
                    visit.add((newRow,newCol))  # ⚠️ mark on push, so it's queued only once

                    res += 1        # each newly reached land cell adds 1 to the area
            return res

        maxArea = 0
        for r in range(nRows):
            for c in range(nCols):
                # ⚠️ add `and (r,c) not in visit`: without it, bfs re-runs from every
                #    cell of an already-measured island (returns 1, so max is still right,
                #    but it's wasted work)
                if grid[r][c]==1 and (r,c) not in visit:
                    area = bfs(r,c)
                    maxArea = max(maxArea, area)
        
        return maxArea

# Time: O(rows * cols), Space: O(rows * cols) for visit + queue