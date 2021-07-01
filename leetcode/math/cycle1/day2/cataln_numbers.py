"""
q:
Given an integer n, return the number of structurally unique BST's 
(binary search trees) 
which has exactly n nodes of unique values from 1 to n.
Example 1:
Input: n = 3
Output: 5

"""
"""
brute force: applying catalan series.
time limit exceded
time took > 5000 ms

"""

class Solution:
    def numTrees(self, n: int) -> int:
        if n <= 1:
            return 1
        res = 0
        for i in range(n):
            res += self.numTrees(i) * self.numTrees(n-i-1)
        return res
"""
better time  and space complexity using cached algorthim & catalan numbers.
Runtime: 32 ms, faster than 56.31% of Python3 online submissions for Unique Binary Search Trees.
Memory Usage: 13.9 MB, less than 97.55% of Python3 online submissions for Unique Binary Search Trees.
Why this works ? 
We are using the same recursion algorithm, but with memoization / applied cache.
https://en.wikipedia.org/wiki/Catalan_number#:~:text=In%20combinatorial%20mathematics%2C%20the%20Catalan,Catalan%20(1814%E2%80%931894).&text=(sequence%20A000108%20in%20the%20OEIS).

"""

class Solution:
    def numTrees(self, n: int) -> int:
        cache = {}
        def catalan(n):
            if n in cache:
                return cache[n]
            if n <= 1:
                return 1
            res = 0
            for i in range(n):
                res += catalan(i) * catalan(n-i-1)
            cache[n] = res
            return res
        return catalan(n)

