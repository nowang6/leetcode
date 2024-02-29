# https://leetcode.com/problems/search-a-2d-matrix/

from typing import List
import math

class Solution:
    def get_matrix_xy(self, m,n,index):
        x = math.floor(index / n)
        y = index % n
        return [x,y]
        
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l, r = 0, (m*n) -1
        while l <= r:
            mid_index = (l+r) // 2
            x, y = self.get_matrix_xy(m, n, mid_index)
            mid_value = matrix[x][y]
            if target == mid_value:
                return True
            elif target < mid_value:
                r = mid_index -1
            else:
                l = mid_index + 1
        return False

s = Solution()
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
res = s.searchMatrix(matrix,3)
print(res)
