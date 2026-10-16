"""
Flood Fill (NeetCode)
=====================

You are given an image represented by an m x n grid of integers image, where
image[i][j] is the pixel value of the image. You are also given three integers
sr, sc, and color.

Perform a flood fill starting from the pixel image[sr][sc]: change the color
of the starting pixel, and of every pixel connected to it horizontally or
vertically that has the same original color, to color.

Return the modified image.

Example 1:
    Input:  image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
    Output: [[2,2,2],[2,2,0],[2,0,1]]
    Explanation: Every 1 connected to the center pixel (1,1) becomes 2. The
    bottom-right 1 isn't connected (only diagonally), so it stays 1.

Example 2:
    Input:  image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
    Output: [[0,0,0],[0,0,0]]
    Explanation: The starting pixel already has color 0, so nothing changes.

Constraints:
    m == image.length
    n == image[i].length
    1 <= m, n <= 50
    0 <= image[i][j], color < 2^16
    0 <= sr < m
    0 <= sc < n

Explanation:

    Same spreading search as Count Number of Islands, but from ONE given start
    instead of looping over every cell: "land" = originalColor, and marking a
    cell = recoloring it.

    Example 2 is the trap: when color == originalColor, a recolored cell still
    looks unvisited, so you need visit (or return early if the colors match).
"""

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