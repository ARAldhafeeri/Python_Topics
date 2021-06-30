"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0

"""







class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        if (nums.count(target) == 1):
            return nums.index(target)
        elif (nums[-1] < target):
            return len(nums)
        else:

            for i in range(0,len(nums)):
                if( nums[i] < target):
                    continue
                else:
                    break
            return i
