# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
"""
| ____ ____ ____ ____ || ____ ____ ____ ____ |
   l1             r1      l2             r2

[l1, r1]旋转数组的前半部分
                            => 满足 l1 > r2
[l2, r2]旋转数组的后半部分

"""
class Solution:
    def search(self, nums: list, target: int) -> int:
        left, right = 0, len(nums) - 1
        while(left <= right):
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            # 中点值大于左侧值
            if nums[mid] >= nums[left]:
                # 如果搜索的值大于左侧
                if target >= nums[left] and target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if target <= nums[right] and nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

# [7,0,1,2,3,4,5]
if __name__ == '__main__':
    nums = [4,5,6,7,0,1,2]
    target = 3
    nums = [1,3]
    target = 3
    sol = Solution()
    print(sol.search(nums, target))