"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Runtime: 76 ms, faster than 53.54% of Python3 online submissions for Minimum Size Subarray Sum.
Memory Usage: 16.5 MB, less than 92.57% of Python3 online submissions for Minimum Size Subarray Sum.
"""

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        left = total = 0
        res = len(nums) + 1
        for i in range(len(nums)):
            total = total + nums[i]
            while total >= s:
                res = min(res,i-left+1)
                total = total - nums[left]
                left = left+1
        return res if res <= len(nums) else 0