class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        left = 0
        m = len(matrix)
        n = len(matrix[0])
        right = m*n - 1

        while left <= right:
            mid = (left + right)//2

            r = mid//n
            c = mid % n

            if matrix[r][c] == target:
                return True
            if matrix[r][c] < target:
                left = mid + 1
            if matrix[r][c] > target :
                right = mid -1 
        return False
        