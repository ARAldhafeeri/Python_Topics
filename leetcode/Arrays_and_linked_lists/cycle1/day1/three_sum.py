"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Runtime: 772 ms, faster than 83.59% of Python3 online submissions for 3Sum.
Memory Usage: 17.3 MB, less than 85.66% of Python3 online submissions for 3Sum.
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums = sorted(nums)
        for i in range(len(nums)-2):
            left = i + 1; right = len(nums) - 1
            target = 0 - nums[i]
            if i == 0 or nums[i] != nums[i-1]:
                while left < right:
                    s = nums[left] + nums[right]
                    if s == target:
                        ans.append([nums[i], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1
                        left += 1; right -=1
                    elif s < target:
                        left += 1
                    else:
                        right -= 1
        return ans