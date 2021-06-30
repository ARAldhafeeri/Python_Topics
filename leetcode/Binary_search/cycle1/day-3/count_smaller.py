"""
315, hard
You are given an integer array nums and you have to return a new counts array. 
The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

 
Example 1:
Input: nums = [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element

"""

"""
sol 1: brute force 
time complexity O(N)
space complexity O(N)
Time limit exceeded.
"""

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        ans = []
        count = 0
        n = len(nums)
        for i in range(0, n):
            for j in range(i, n):
                if nums[j] < nums[i]:
                    count += 1
            ans.append(count)
            count = 0
        return ans
                
"""
using bitsection algorithm 
solution Credits to @Celine00. 
"""

import bisect as bi

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        res, arr = [], []
        for n in nums[::-1]:
            idx = bi.bisect_left(arr, n)
            res.append(idx)
            arr.insert(idx, n)
        return res[::-1]

