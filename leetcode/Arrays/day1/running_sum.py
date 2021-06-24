"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
Runtime: 36 ms, faster than 86.03% of Python3 online submissions for Running Sum of 1d Array.
Memory Usage: 14.5 MB, less than 39.37% of Python3 online submissions for Running Sum of 1d Array.
"""
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(1, n):
            nums[i] += nums[i - 1]
        return nums
            
            
