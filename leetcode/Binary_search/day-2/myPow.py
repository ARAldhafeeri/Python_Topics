
"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
"""

"""
sol 1: brute force
apply how the power work based on mathmatical concept.
time complexity 
since we divide n by 2 over and over again then ON(logn)
space complexity O(N^2) because we are storing foalt x,y, and multiply them x * x = x^2
Runtime: 28 ms, faster than 84.41% of Python3 online submissions for Pow(x, n).
Memory Usage: 14.4 MB, less than 15.45% of Python3 online submissions for Pow(x, n).
"""
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        if n == 0:
            return 1
        y = 1
        while n > 1:
            if n % 2 == 0:
                x *= x
                n /= 2
            else:
                y *= x
                x *= x
                n = (n - 1) /2
        return x * y