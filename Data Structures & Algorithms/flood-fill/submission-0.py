class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        nRows, nCols = len(image), len(image[0])
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        originalColor = image[sr][sc]   # only cells with this color get filled
        visit = set()

        # spreads from (r,c) to every connected cell of originalColor and recolors it
        def dfs(r,c):
            # stop: off the grid, a different color, or already filled
            if r<0 or r==nRows or c<0 or c==nCols or image[r][c]!=originalColor or (r,c) in visit:
                return

            image[r][c] = color
            # ⚠️ visit matters when color == originalColor: a recolored cell still
            #    matches originalColor, so without it the search never stops
            #    e.g. image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
            visit.add((r,c))

            for dr,dc in directions:
                newRow, newCol = r+dr, c+dc
                dfs(newRow, newCol)

        dfs(sr, sc)                     # ⚠️ start at the given pixel, not (0,0)
        return image

# Time: O(rows * cols), Space: O(rows * cols) for visit + recursion