class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        top = 0
        bottom = len(matrix) - 1

        while top <= bottom:
            mid = top + (bottom - top)//2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                top = mid + 1
            else:
                bottom = mid - 1
        
        row = bottom
        if row < 0:
            return False    
            
        low = 0
        high = len(matrix[0]) - 1

        while low <= high:
            mid = low + ((high - low)//2)

            if target > matrix[row][mid]:
                low = mid + 1
            elif target < matrix[row][mid]:
                high = mid - 1
            else:
                return True

        return False





                