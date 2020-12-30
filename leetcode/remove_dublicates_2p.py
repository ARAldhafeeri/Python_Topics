"""
Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.

Do not allocate extra space for another array; you must do this by modifying the input array in-place with O(1) extra memory.

Clarification:

Confused why the returned value is an integer, but your answer is an array?

Note that the input array is passed in by reference, which means a modification to the input array will be known to the caller.

Internally you can think of this:

"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        for i in range(len(nums) - 1,0, -1):
            if len(nums)>2 and nums[i] == nums[i-1] and nums[i-1]== nums[i-2]:
                nums.pop(i)
                ++j
                continue
            if len(nums)>2 and nums[j] == nums[j+1] and nums[j+1]== nums[j+2]:
                nums.pop(j)
                ++j
