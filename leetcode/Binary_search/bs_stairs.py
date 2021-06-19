"""
ou have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build.

 

Example 1:


Input: n = 5
Output: 2
Explanation: Because the 3rd row is incomplete, we return 2.
Example 2:


Input: n = 8
Output: 3
Explanation: Because the 4th row is incomplete, we return 3.
"""

"""
sol 1 : brute force itertive

Runtime: 1020 ms, faster than 37.84% of Python3 online submissions for Arranging Coins.
Memory Usage: 14 MB, less than 86.17% of Python3 online submissions for Arranging Coins

Time complexity: 
O(N - 1)
removing constants
O(N)

Space Compexity:
two variables 4 bytes type int
O(3S)
Removing constants 
O(S)

"""
class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n  == 1:
            return 1
        stairs = 0
        for i in range(1, n):
            n = n - i
            if n >= 0:
                stairs += 1
            else:
                break
        return stairs

""" 
sol 2: Binary search
  Runtime: 24 ms, faster than 99.32% of Python3 online submissions for Arranging Coins.
  Memory Usage: 14.2 MB, less than 63.99% of Python3 online submissions for Arranging Coins.

  Time complexity:
  n/2
  n/4
  n/8 
  .......
  therefore 
  O(long2N)
  Space complexity:
  since we are using l,r, row, curr
  which are integer variables 4 bytes
  no matter what...
  then space complexity is constant
  O(1)

"""
class Solution:
    def arrangeCoins(self, n: int) -> int:
        l = 0
        r = n
        while( l <= r):
            row = (l + r) // 2
            curr = row * (row + 1) // 2
            if curr == n:
                return row
            if n < curr:
                r = row - 1
            else:
                l = row + 1
        return r

""" 
sol 3: math:

Runtime: 24 ms, faster than 99.32% of Python3 online submissions for Arranging Coins.
Memory Usage: 14.2 MB, less than 63.99% of Python3 online submissions for Arranging Coins.

Time complexity:
Since we are preforming one step as mathmatical equation.
then time complexity is constant
O(1)
Since we are only using one variable then space complexity is constant
O(1)

"""

class Solution:
    def arrangeCoins(self, n: int) -> int:
        return (int)((2 * n + 0.25)**0.5 - 0.5)
