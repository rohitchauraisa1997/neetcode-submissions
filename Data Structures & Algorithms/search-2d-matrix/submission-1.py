class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:   
        n_rows = len(matrix)
        n_cols = len(matrix[0])

        top = 0
        bottom = n_rows-1

        while top<=bottom:
            mid_row = (top+bottom)//2
            if matrix[mid_row][-1] < target:
                top = mid_row+1
            elif matrix[mid_row][0] > target:
                bottom = mid_row-1
            else:
                break
        
        if not (top <= bottom):
            return False
        
        mid = (top+bottom)//2
        row = matrix[mid]
        l = 0
        r = len(row)-1

        while l<=r:
            mid = (l+r)//2
            if row[mid] < target:
                l = mid+1
            elif row[mid] > target:
                r = mid-1
            else:
                return True

        return False
