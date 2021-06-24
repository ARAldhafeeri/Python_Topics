"""
Runtime: 44 ms, faster than 98.44% of Python3 online submissions for Richest Customer Wealth.
Memory Usage: 14.3 MB, less than 26.36% of Python3 online submissions for Richest Customer Wealth.
"""



class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max([sum(i) for i in accounts])

