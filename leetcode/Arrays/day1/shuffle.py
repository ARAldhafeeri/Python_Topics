"""
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].

 

Example 1:

Input: nums = [2,5,1,3,4,7], n = 3
Output: [2,3,5,4,1,7] 
Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].
Runtime: 60 ms, faster than 67.42% of Python3 online submissions for Shuffle the Array.
Memory Usage: 14.2 MB, less than 91.47% of Python3 online submissions for Shuffle the Array.
"""

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        for i in range(0, len(nums) - n ):
            ans.append(nums[i])
            ans.append(nums[n])
            n += 1
        return ans