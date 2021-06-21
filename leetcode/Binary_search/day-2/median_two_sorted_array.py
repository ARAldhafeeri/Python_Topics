""" Hard problem
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

"""

"""
sol 1: brute force buble sort:
time complexity O(N^2)
space complexity O(1)

Runtime: 3020 ms, faster than 5.39% of Python3 online submissions for Median of Two Sorted Arrays.
Memory Usage: 14.6 MB, less than 52.23% of Python3 online submissions for Median of Two Sorted Arrays.

"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nl = nums1 + nums2
        n = len(nl)
        mid = n // 2
        print(nl)
        for i in range(n - 1):
            k = n - i - 1
            for j in range(0, k):
                if nl[j] > nl[j+1]:
                    nl[j], nl[j + 1] = nl[j + 1], nl[j]
        if n % 2 == 1:
            return float(nl[mid])
        else:
            return ((nl[mid] + nl[mid -1]) / 2)

"""
sol 2 using python sorted ( timsort) / merge sort
time complexity: O(nlog2n)
space complexity: O(1)

Runtime: 84 ms, faster than 94.09% of Python3 online submissions for Median of Two Sorted Arrays.
Memory Usage: 14.7 MB, less than 21.35% of Python3 online submissions for Median of Two Sorted Arrays.
"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nl = nums1 + nums2
        n = len(nl)
        mid = n // 2
        nl = sorted(nl)
        if n % 2 == 1:
            return float(nl[mid])
        else:
            return ((nl[mid] + nl[mid -1]) / 2)
                