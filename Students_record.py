"""
Given a positive integer n, return the number of all possible attendance records with length n, which will be regarded as rewardable. The answer may be very large, return it after mod 109 + 7.

A student attendance record is a string that only contains the following three characters:

'A' : Absent.
'L' : Late.
'P' : Present.
A record is regarded as rewardable if it doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

Example 1:
Input: n = 2
Output: 8 
Explanation:
There are 8 records with length 2 will be regarded as rewardable:
"PP" , "AP", "PA", "LP", "PL", "AL", "LA", "LL"
Only "AA" won't be regarded as rewardable owing to more than one absent times. 
"""

from itertools import product     
class Solution:
    def checkRecord(self, n: int) -> int:
        M = 1e9 + 7
        A0L0 = 1
        A0L1 = 0
        A0L2 = 0
        A1L0 = 0
        A1L1 = 0
        A1L2 = 0
        
        for _ in range(n + 1):
            A0L1, A0L2, A0L0 = A0L0, A0L1, (A0L0 + A0L1 + A0L2) % M
            A1L2, A1L1, A1L0 = A1L1, A1L0, (A0L0 + A1L0 + A1L1 + A1L2) % M

        return int(A1L0)
                
