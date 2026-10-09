class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n_rows = len(matrix)
        n_cols = len(matrix[0])   # unused; can be removed

        # Step 1: binary search over ROWS to find the one that could contain target
        top = 0
        bottom = n_rows - 1

        while top <= bottom:
            mid_row = (top + bottom) // 2
            if matrix[mid_row][-1] < target:     # target bigger than row's max → go down
                top = mid_row + 1
            elif matrix[mid_row][0] > target:    # target smaller than row's min → go up
                bottom = mid_row - 1
            else:                                # row[0] <= target <= row[-1] → found the row
                break

        # loop ended without break → no row's range contains target
        if not (top <= bottom):
            return False

        # Step 2: binary search WITHIN that row
        mid = (top + bottom) // 2   # same as mid_row (top/bottom unchanged after break)
        row = matrix[mid]
        l = 0
        r = len(row) - 1

        while l <= r:
            mid = (l + r) // 2
            if row[mid] < target:
                l = mid + 1
            elif row[mid] > target:
                r = mid - 1
            else:
                return True

        return False