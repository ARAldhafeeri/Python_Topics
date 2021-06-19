"""
ou have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build.

 

Example 1:


Input: n = 5
Output: 2
Explanation: Because the 3rd row is incomplete, we return 2.
Example 2:


Input: n = 8
Output: 3
Explanation: Because the 4th row is incomplete, we return 3.
"""


"""
sol 1 : brute force hashtable

Runtime: 108 ms, faster than 72.10% of Python3 online submissions for The K Weakest Rows in a Matrix.
Memory Usage: 14.6 MB, less than 45.53% of Python3 online submissions for The K Weakest Rows in a Matrix

time complexity O(N)
space complexity O(N)

"""
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        hashtable = {}
        ans = []
        n = len(mat)
        for i in range(0, n):
            curr = mat[i]
            ones = curr.count(1)
            hashtable[i] = ones
        weekest_to_strongest = sorted(hashtable.items(), key=lambda x: x[1], reverse=False)
        for i in range(k):
            ans.append(weekest_to_strongest[i][0])
        return ans
            

"""
sol 2 : bubble sort

Runtime: 108 ms, faster than 72.10% of Python3 online submissions for The K Weakest Rows in a Matrix.
Memory Usage: 14.6 MB, less than 45.53% of Python3 online submissions for The K Weakest Rows in a Matrix

time complexity O(N)
space complexity O(N)

"""
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        n = len(mat)
        ones = [sum(i) for i in mat]
        indexes = [i for i in range(n)]
        for i in range(0, n):
            for j in range(0, n - i - 1):
                if ones[j] > ones[j+1]:
                    ones[j], ones[j+1] = ones[j+1], ones[j]
                    indexes[j], indexes[j+1] = indexes[j+1], indexes[j]
        return indexes[0:k]
            
            
        
            
            
            
