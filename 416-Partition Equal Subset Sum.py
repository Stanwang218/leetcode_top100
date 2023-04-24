# Input: nums = [1,5,11,5]
# Output: True
"""
dp方法:

2-Dimension

dp[i][j] 表示到下标为i的num，是否满足和为j
dp[i][j]满足性质：
1. if dp[i-1][j] = True => dp[i][j] = True

不选择num[i]即可

2. if dp[i-1][j] = False => dp[i][j] = dp[i - 1][j - nums[i]]

即选择nums[i]，则前i-1项的和为j-nums[i]

1-Dimension
dp[i] 表示是否满足和为i

结果返回 dp[target_sum]

对于每一个num，i从target_sum循环到num => dp[i] = dp[i] or dp[i - num]
"""
class Solution:
    def canPartition(self, nums: list) -> bool:
        s = sum(nums)
        if s % 2 == 1:
            return False
        target_sum = s // 2
        dp = [True] + [False] * target_sum
        for num in nums:
            for temp in range(target_sum, num-1, -1):
                dp[temp] = dp[temp] or dp[temp - num]
        return dp[target_sum]

if __name__ == '__main__':
    sol = Solution()
    nums = [1,5,11,5]
    print(sol.canPartition(nums))