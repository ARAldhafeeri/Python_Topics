"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

 

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
"""

"""
sol 1: brute force
time limit exceeded

"""
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ans = []
        for i in nums:
            if nums.count(i) > 1:
                return i

"""
sol 2: fast and slow pointer :
Runtime: 616 ms, faster than 60.29% of Python3 online submissions for Find the Duplicate Number.
Memory Usage: 28 MB, less than 75.83% of Python3 online submissions for Find the Duplicate Number.
"""


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[nums[0]]
        while fast != slow:
            slow = nums[slow] # move one step for slow
            fast = nums[nums[fast]] # move two steps for fast
        
        fast = 0 # find entry point to cycle
        while ( slow != fast):
            slow = nums[slow]
            fast = nums[fast]
        return slow