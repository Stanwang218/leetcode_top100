# Input:
# ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
# [[], [1], [2], [], [3], []]
# Output:
# [null, null, null, 1.5, null, 2.0]

from heapq import *
# the default heap is small heap
# heapq库中只有小根堆，若要使用大根堆，push元素时push相反数
# Ensure that the size of small heap is one element larger than large heap
# 保证小根堆元素个数比大根堆元素个数大1
# Small heap stores half numbers that are large
# large heap contains the other half numbers that are small
# 小根堆存大的数，堆顶为大数中的最小值
# 大根堆存小的数，堆顶为小数中的最大值
class MedianFinder:

    def __init__(self):
        self.lh, self.sh = [], []

    def addNum(self, num: int) -> None:
        heappush(self.lh, -num)
        heappush(self.sh, -self.lh[0])
        heappop(self.lh)
        if len(self.lh) < len(self.sh):
            heappush(self.lh, -self.sh[0])
            heappop(self.sh)

    def findMedian(self) -> float:
        if len(self.lh) > len(self.sh):
            return -self.lh[0]
        else:
            return (-self.lh[0] + self.sh[0]) / 2.0

if __name__ == '__main__':
    sol = MedianFinder()
    op_code = ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
    op = [[], [1], [2], [], [3], []]
    # op_code = ["MedianFinder","addNum","findMedian"]
    # op = [[],[1],[]]
    for i, item in enumerate(op_code):
        if item == "MedianFinder":
            print(MedianFinder())
        elif item == "addNum":
            print(sol.addNum(op[i][0]))
        else:
            print(sol.findMedian())
