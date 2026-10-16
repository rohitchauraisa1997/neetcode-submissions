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