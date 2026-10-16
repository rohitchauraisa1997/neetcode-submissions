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