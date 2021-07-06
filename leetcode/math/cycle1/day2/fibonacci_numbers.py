"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.

"""

"""
sol 1: applying the eq using recursion

Runtime: 800 ms, faster than 22.84% of Python3 online submissions for Fibonacci Number.
Memory Usage: 14.3 MB, less than 7.66% of Python3 online submissions for Fibonacci Number.
"""
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)

"""
sol 2: cache version
Runtime: 32 ms, faster than 64.23% of Python3 online submissions for Fibonacci Number.
Memory Usage: 14.1 MB, less than 68.94% of Python3 online submissions for Fibonacci Number.
"""
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        res = [0,1]
        for i in range(2,n+1):
            res.append(res[-1] + res[-2])       
        return res[-1]
        