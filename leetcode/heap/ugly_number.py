import heapq
class Solution:
    def nthUglyNumber(self, n):
        q2, q3, q5 = [2], [3], [5]
        ugly = 1
        for u in heapq.merge(q2, q3, q5):
            if n == 1:
                return ugly
            if u > ugly:
                ugly = u
                n -= 1
                q2 += 2 * u,
                q3 += 3 * u,
                q5 += 5 * u,


"""
Given an integer n, return the nth ugly number.

Ugly number is a positive number whose prime factors only include 2, 3, and/or 5.

 

Example 1:

Input: n = 10
Output: 12
Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.

Runtime: 228 ms, faster than 31.62% of Python3 online submissions for Ugly Number II.
Memory Usage: 14.4 MB, less than 50.26% of Python3 online submissions for Ugly Number II.

"""