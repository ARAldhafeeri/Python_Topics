class Solution:
    def maxSubArray(self, nums: list(int)) -> int:
        if not nums:
            return 0

        if len(nums) == 1:
            return sum(nums)
        else:
            max_current = max_global = nums[0]
            for i in range(0, len(nums)):
                max_current = max(nums[i], max_current + nums[i])
                if max_current > max_global:
                    max_global = max_current

            return max_global


if __name__ == '__main__':
    s = int(input())
    a = Solution()
    print(a.maxSubArray(s))