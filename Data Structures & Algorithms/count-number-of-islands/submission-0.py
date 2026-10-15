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