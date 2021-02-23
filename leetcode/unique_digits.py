
"""
Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.

Example:

Input: 2
Output: 91 
Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100, 
             excluding 11,22,33,44,55,66,77,88,99
 

Constraints:

0 <= n <= 8

"""

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 10
        if n == 2:
            return 91
        # 9 * 9 = 81
        prod = 81
        end = 8 
        # current value is 91 we start from n = 3
        curr = 91
        prev = 81
        # passed 0 -> 2
        step = 3
        while(step <= n):
            prod *= end
            end -= 1
            prev = curr
            curr = prod
            curr += prev
            step += 1
        return curr