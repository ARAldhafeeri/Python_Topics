import heapq
from collections import Counter
"""
Problem:
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1: return [nums[0]]
        hashtable = Counter(nums)
        return heapq.nlargest(k, hashtable.keys(), key=hashtable.get)
