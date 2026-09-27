class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW, COL = len(matrix), len(matrix[0])

        top, bot = 0, ROW -1 

        while top <= bot: 
            midROW = (bot + top) // 2
            if target > matrix[midROW][-1]:
                top = midROW + 1
            elif target < matrix[midROW][0]:
                bot = midROW - 1
            else: 
                break
        
        if not (top <= bot):
            return False
        
        midROW = (bot + top) // 2
        l, r = 0, COL - 1
        
        while l <= r: 
            m = (l + r) // 2
            if target < matrix[midROW][m]: 
                r = m - 1
            elif target > matrix[midROW][m]: 
                l = m + 1
            else:  
                return True

        return False
