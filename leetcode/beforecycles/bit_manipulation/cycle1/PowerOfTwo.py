"""
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.

"""

# naive and slow, sol
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        for i in range(32):
            if 2**i == n:
                return True
        return False