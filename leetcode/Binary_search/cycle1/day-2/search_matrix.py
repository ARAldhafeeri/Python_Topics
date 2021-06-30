"""


"""
"""
sol 1: binary search with transforming 2D matrix into 1D
Runtime: 36 ms, faster than 95.52% of Python3 online submissions for Search a 2D Matrix.
Memory Usage: 15 MB, less than 29.00% of Python3 online submissions for Search a 2D Matrix.

Time complexity O(logn)
space complexity 1D array O(N)
"""

class Solution:
    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
        m = len(mat)
        n = len(mat[0])
        if target < mat[0][0] or target > mat[m - 1][n - 1]:
            return False
        flat =[ i for sublist in mat for i in sublist]
        l = 0
        r = len(flat)
        while( l <= r):
            mid = (l + r) // 2
            if( target == flat[mid]):
                return True
            elif( target < flat[mid]):
                r = mid - 1
            else:
                l = mid + 1
        return False
                