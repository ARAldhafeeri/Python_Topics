import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        for _ in range(len(nums) - k):
            heapq.heappop(nums)
        return nums[0]


"""
question:

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

performance :
Runtime: 60 ms, faster than 87.82% of Python3 online submissions for Kth Largest Element in an Array.
Memory Usage: 15.1 MB, less than 74.71% of Python3 online submissions for Kth Largest Element in an Array.
"""
