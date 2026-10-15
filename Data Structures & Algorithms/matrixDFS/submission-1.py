class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        nRows, nCols = len(grid),len(grid[0])
        visit = set()               # cells on the CURRENT path, shared by all calls

        def dfs(r,c):
            # dead end: off the grid, already on this path, or a wall (1)
            # ⚠️ == nRows / == nCols, since valid indices are 0..n-1
            if (r<0 or r==nRows 
                or c<0 or c==nCols 
                or (r,c)in visit 
                or grid[r][c]==1):
                return 0
            
            # reached bottom-right: this path counts once
            # ⚠️ return before visit.add, so there's nothing to undo here
            if r==nRows-1 and c==nCols-1:
                return 1

            visit.add((r,c))        # CHOOSE: put this cell on the path
            
            count = 0
            dirs = [(0,1),(1,0),(0,-1),(-1,0)]   # right, down, left, up

            # EXPLORE: add up the paths from every neighbour (count all, no early return)
            for dr, dc in dirs:
                row, col = r+dr, c+dc
                count += dfs(row,col)

            # UN-CHOOSE: ⚠️ other paths may pass through this cell, so free it again
            # (a permanent visited set, as in Number of Islands, would undercount)
            visit.remove((r,c))
        
            return count
    
        return dfs(0,0)

# Time: O(4^(rows*cols)) worst case, every path is explored
# Space: O(rows*cols) for the recursion and visit