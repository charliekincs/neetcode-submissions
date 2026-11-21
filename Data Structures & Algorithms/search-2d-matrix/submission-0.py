class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        bottom, top = 0, len(matrix) - 1
        l, r = 0, len(matrix[0]) - 1
        mid_row = (top + bottom) // 2
        while bottom <= top:
            mid_row = (top + bottom) // 2

            if target < matrix[mid_row][l]:
                top = mid_row - 1
            elif target > matrix[mid_row][r]:
                bottom = mid_row + 1
            else:
                break
            
        if target < matrix[mid_row][l] or target > matrix[mid_row][r]:
            return False

        while l <= r:
            mid_col = (l + r) // 2

            if matrix[mid_row][mid_col] == target:
                return True
            if target < matrix[mid_row][mid_col]:
                r = mid_col - 1
            else:
                l = mid_col + 1
        
        return False