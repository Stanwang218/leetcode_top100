# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]

from typing import *

def twoSum(nums: List[int], target: int) -> List[int]:
    # key represents the target - num
    # 键代表目标与当前数字的差
    # value represents the index of the num
    # 值代表当前数字的下标
    d = dict()
    for i, item in enumerate(nums):
        # if the current element is in the dictionary, target - item is already found
        # 如果当前元素位于字典，target - item 已经遍历过了
        if item in d:
           return [i , d[item]]
        else:
            d[target - item] = i
    return None


if __name__ == '__main__':
    nums = [2,7,11,15]
    target = 9
    print(twoSum(nums, target))