from typing import *
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    ans = []
    target = -nums[0]
    # sort the list and choose each element as the target
    # if the target is the same with the last one, ignore it !
    # 选取每个元素为目标元，如何当前元素与上一个元素相同，则跳过
    for i, item in enumerate(nums):
        if -item == target and i != 0:
            continue
        target = -item
        l,r = i + 1, len(nums) - 1
        while l < r:
            if nums[l] + nums[r] > target:
                r -= 1
            elif nums[l] + nums[r] < target:
                l += 1
            else:
                # focus on this part !
                # 重点
                
                # temp.sort()           # these two lines are original
                # if temp not in ans:   # the following line optimizes the method          
                
                temp = [-target, nums[l], nums[r]]
                ans.append(temp)
                
                # if element l + 1 and l have same elements, ignore it as well
                # 如果[l+1]与[l]所在下标的两个数相同，则跳过
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                l += 1
    return ans


if __name__ == '__main__':
    # nums = [-1,0,1,2,-1,-4]
    nums = [-2,0,0,2,2]
    print(threeSum(nums))