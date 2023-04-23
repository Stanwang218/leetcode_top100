# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
from collections import deque
"""
使用deque 双端队列 保证队列单调（monotonic）
队列的头部为窗口的最大值！
每次入队的元素保证是当前队中的最大值
"""
class Solution:
    def maxSlidingWindow(self, nums: list, k: int) -> list:
        dq = deque()
        ans = []
        for j, item in enumerate(nums):
            # 弹出比当前元素小的元素
            while len(dq) > 0 and nums[dq[-1]] < item:
                dq.pop()
            dq.append(j)
            # 如果队列中的头部元素最大，但是超出了窗口的大小，进行弹出
            if dq[0] == j - k:
                dq.popleft()
            # 如果当前元素的下标大于窗口大小减1，则窗口填满元素，保存队列头部元素
            if j >= k-1:
                ans.append(nums[dq[0]])
        return ans


if __name__ == '__main__':
    sol = Solution()
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    print(sol.maxSlidingWindow(nums, k))