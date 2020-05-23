# given an array = [1,2,3,4] find the two indexes in a list [0,1] that return 3

class Solution:
    # Function defintion with types and returning value type ?
    def twoSum(self, nums: List[int], target: int) -> List[int]:


        dic = {}
        for i, n in enumerate(nums):
            if n in dic:
                return [dic[n], i]
            dic[target-n] = i
