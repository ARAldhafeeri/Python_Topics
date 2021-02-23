class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        ans = []
        [ans.append(i) for i in range(1, n + 1) if n % i == 0]
        if k > len(ans):
            return -1
        else:
            return ans[k -1]
            
        