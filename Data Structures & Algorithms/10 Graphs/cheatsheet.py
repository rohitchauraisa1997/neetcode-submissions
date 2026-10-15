"""
GRAPHS: MATRIX DFS / BFS CHEATSHEET

1. Two kinds of matrix DFS. The only difference in code is whether you undo the visit.

  |                | Reachability / flood fill    | Path counting / finding         |
  |----------------|------------------------------|---------------------------------|
  | Question       | Which cells can I reach?     | How many ways (or which ways)?  |
  | `visit` means  | visited ever                 | on the CURRENT path             |
  | Undo?          | No, stays visited            | Yes, visit.remove() (backtrack) |
  | Each cell      | processed once               | once per path through it        |
  | Time           | O(rows * cols)               | O(4^(rows * cols))              |
  | Examples       | Number of Islands, Max Area  | Count Paths (matrixDFS),        |
  |                | of Island, Rotting Oranges   | Word Search                     |

  How to tell: should two different routes to the same cell count separately?
    - No  -> mark once, never unmark. Plain DFS (or BFS).
    - Yes -> free the cell when you back out of it. Backtracking
             (see the Backtracking cheatsheet).

  If you may only move right/down, paths can't loop back: no `visit` needed, and
  many paths reach the same cell, so cache each cell's result. That's DP
  (Unique Paths): O(rows * cols) instead of exponential.

2. BFS vs DFS with a deque: just which end you pop from.

    row, col = q.popleft()   # queue (FIFO): BFS, spreads out ring by ring
    row, col = q.pop()       # stack (LIFO): DFS, follows one direction deep first

  For reachability (Number of Islands) both give the same answer and O(rows * cols).
  Only BFS gives shortest paths in an unweighted grid (Shortest Path in Binary
  Matrix, Rotting Oranges), because it reaches cells in order of distance.

3. Mark visited when you PUSH, not when you pop.
    - Marking on pop lets the same cell be pushed many times by different
      neighbours. Still correct, but slower and uses more memory.
    - With mark-on-push, the stack version isn't exactly recursive DFS order
      (the first neighbour to push a cell claims it). Fine for reachability; use
      real recursion when the order matters (cycle detection, topological sort).

4. Recursion depth.
    Recursive DFS on a big all-land grid (300 x 300 = 90,000 cells) goes ~90,000
    calls deep. Python's default limit is ~1,000, so it crashes. Use a stack
    (q.pop()) or BFS for large grids.

⚠️ Common mistakes:
  1. Bounds: valid indices are 0..rows-1, so check r == rows (or r >= rows), not r > rows.
  2. Check bounds BEFORE grid[r][c], or a negative index silently wraps around in Python.
  3. Forgetting visit.remove() in path counting -> undercounts.
     Adding visit.remove() in flood fill -> exponential time.
  4. Counting islands: start a new search only from unvisited land, then islands += 1.
"""

from collections import deque

DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]      # down, up, right, left


# ---------------------------------------------------------------------------
# FLOOD FILL (reachability): visit stays marked. O(rows * cols)
# ---------------------------------------------------------------------------
def numIslands(grid):
    rows, cols = len(grid), len(grid[0])
    visit = set()

    def explore(r, c):
        q = deque([(r, c)])
        visit.add((r, c))                       # mark on push
        while q:
            row, col = q.popleft()              # popleft = BFS, pop = DFS; same count
            for dr, dc in DIRS:
                nr, nc = row + dr, col + dc
                if (0 <= nr < rows and 0 <= nc < cols
                        and grid[nr][nc] == "1" and (nr, nc) not in visit):
                    visit.add((nr, nc))
                    q.append((nr, nc))

    islands = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visit:
                explore(r, c)                   # marks the whole island
                islands += 1
    return islands


# ---------------------------------------------------------------------------
# PATH COUNTING (backtracking): visit is undone on the way back. O(4^(rows*cols))
# ---------------------------------------------------------------------------
def countPaths(grid):
    rows, cols = len(grid), len(grid[0])
    visit = set()                               # cells on the CURRENT path

    def dfs(r, c):
        if (min(r, c) < 0 or r == rows or c == cols
                or (r, c) in visit or grid[r][c] == 1):
            return 0
        if r == rows - 1 and c == cols - 1:
            return 1

        visit.add((r, c))                       # CHOOSE
        count = sum(dfs(r + dr, c + dc) for dr, dc in DIRS)   # EXPLORE
        visit.remove((r, c))                    # UN-CHOOSE
        return count

    return dfs(0, 0)
