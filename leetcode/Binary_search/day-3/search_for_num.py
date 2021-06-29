"""

Runtime: 44 ms, faster than 98.49% of Python3 online submissions for Search in Rotated Sorted Array II.
Memory Usage: 15.1 MB, less than 31.19% of Python3 online submissions for Search in Rotated Sorted Array II.

"""
"""
sol 1 : bruteforce using binary search
time complexity: N(logn)
space complexitgy N(1)

"""
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums) == 1:
            return nums[0] == target
        nums = sorted(nums)
        l = 0
        r = len(nums) - 1
        while( l <= r):
            mid = (l + r ) // 2
            if(nums[mid] == target):
                return True
            elif(nums[mid] > target):
                r = mid - 1
            else:
                l = mid + 1
        return False


        for i in range(len(nums)-2):
            left = i + 1; right = len(nums) - 1
            target = 0 - nums[i]
            if i == 0 or nums[i] != nums[i-1]:
                while left < right:
                    s = nums[left] + nums[right]
                    if s == target:
                        results.append([nums[i], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1
                        left += 1; right -=1
                    elif s < target:
                        left += 1
                    else:
                        right -= 1