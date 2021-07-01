"""
Given two integers left and right, return the count of numbers in the inclusive range [left, right] having a prime number of set bits in their binary representation.

Recall that the number of set bits an integer has is the number of 1's present when written in binary.

For example, 21 written in binary is 10101 which has 3 set bits.
 

Example 1:

Input: left = 6, right = 10
Output: 4
Explanation:
6 -> 110 (2 set bits, 2 is prime)
7 -> 111 (3 set bits, 3 is prime)
9 -> 1001 (2 set bits , 2 is prime)
10->1010 (2 set bits , 2 is prime)


"""
"""
ans :
https://en.wikipedia.org/wiki/Wilson%27s_theorem
idea:
First we convert the number two binary as the problem asked.
Then we count the number of 1 bits.
if the number of bits is not 1
and (n-1)! mod n where n is the number of 1 bits == 1 less than multiple of bits
thus as theorm suggest (n - 1)! mod n == n - 1
Runtime: 236 ms, faster than 74.46% of Python3 online submissions for Prime Number of Set Bits in Binary Representation.
Memory Usage: 14.3 MB, less than 54.70% of Python3 online submissions for Prime Number of Set Bits in Binary Representation.

"""

class Solution:
    def countPrimeSetBits(self, l: int, r: int) -> int:
        ans = 0
        for i in range(l,r+1):
            bits = bin(i).count('1')
            f1=(bits!=1)
            f2=(math.factorial(bits - 1) % bits) == bits -1
            if  f1 and f2 :
                ans += 1
        return ans