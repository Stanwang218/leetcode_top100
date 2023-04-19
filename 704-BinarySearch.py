# Input:[-1,0,3,5,9,12], 9
# Output: 4

"""
right 最后一个元素的索引
查找区间[left, right]
所以 结束判断条件为left<=right
"""
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while(left <= right):
            mid = (left + right) // 2
            # print(mid)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        if nums[mid] != target:
            return -1


if __name__ == '__main__':
    sol = Solution()
    nums = [-1,0,3,5,9,12]
    target = 12
    print(sol.search(nums,target))