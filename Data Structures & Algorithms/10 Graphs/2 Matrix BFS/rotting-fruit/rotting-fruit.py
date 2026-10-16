"""
Rotting Fruit (NeetCode)
========================

You are given a 2-D matrix grid. Each cell can have one of three possible
values:
    - 0 representing an empty cell
    - 1 representing a fresh fruit
    - 2 representing a rotten fruit

Every minute, if a fresh fruit is horizontally or vertically adjacent to a
rotten fruit, then the fresh fruit also becomes rotten.

Return the minimum number of minutes that must elapse until there are zero
fresh fruits remaining. If this state is impossible within the grid, return -1.

Example 1:
    Input: grid = [[1,1,0],[0,1,1],[0,1,2]]
    Output: 4

Example 2:
    Input: grid = [[1,0,1],[0,2,0],[1,0,1]]
    Output: -1
    Explanation: The fresh fruits in the corners are walled off by empty cells.

Constraints:
    1 <= grid.length, grid[i].length <= 10

Explanation:

    Multi-source BFS: queue up EVERY rotten fruit first, so the rot spreads from
    all of them at the same time. One BFS level = one minute.

      minute 0   minute 1   minute 2   (two rotten corners spreading together)
      2 1 1      2 2 1      2 2 2
      1 1 1  ->  2 1 2  ->  2 2 2      answer 2, not 4
      1 1 2      1 2 2      2 2 2

    `fresh` counts what's left: stop when it hits 0 (no extra minute for the
    last level), and if fruit is still fresh when the queue empties, it's -1.
"""

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        nRows, nCols = len(grid), len(grid[0])
        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        queue = deque()
        visit = set()
        time = 0
        fresh =0

        # count fresh oranges, and queue up ALL rotten ones at once, so the rot
        # spreads from every one of them at the same time (multi-source BFS)
        for r in range(nRows):
            for c in range(nCols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    # find all rotten for which bfs will be run
                    queue.append((r,c))
                    visit.add((r,c))
        
        # one BFS level = one minute: everything in the queue now rots its neighbours
        # ⚠️ `and fresh>0`: stop once nothing is left to rot, or the last level
        #    (oranges with no fresh neighbours) adds an extra minute
        while len(queue)>0 and fresh>0:
            for i in range(len(queue)):         # ⚠️ snapshot: only this minute's oranges
                r, c = queue.popleft()
                for dr, dc in directions:
                    newRow, newCol = r+dr, c+dc
                    # ⚠️ skip anything that ISN'T fresh (!= 1): empty (0) and rotten (2),
                    #    plus off the grid / already rotted
                    if (newRow<0 or newRow == nRows or
                        newCol<0 or newCol == nCols or
                        (newRow,newCol) in visit or
                        grid[newRow][newCol] != 1):
                        continue

                    queue.append((newRow, newCol))
                    visit.add((newRow, newCol))   # mark on push, so it rots (and counts) once
                    fresh -= 1                    # one fewer fresh orange
            time += 1                             # this minute's spread is done

            # ALTERNATIVE to `and fresh>0` above: return as soon as the last one rots
            # if fresh == 0:
            #     return time

        # fresh left over = walled off by empty cells, the rot can never reach them
        if fresh==0:
            return time
        else:
            return -1

# Time: O(rows * cols), Space: O(rows * cols)