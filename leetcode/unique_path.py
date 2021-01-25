# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

# How many possible unique paths are there?

 

# Example 1:


# Input: m = 3, n = 7
# Output: 28
# Example 2:

# Input: m = 3, n = 2
# Output: 3
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down
# Example 3:

# Input: m = 7, n = 3
# Output: 28

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = [[-1 for j in range(m)] for i in range(n)]
        if m<2 or n<2:
            return 1
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if i==n-1 or j ==m-1:
                    res[i][j] = 1
                else:
                    res[i][j] = res[i][j+1] + res[i+1][j]
        return res[0][0]