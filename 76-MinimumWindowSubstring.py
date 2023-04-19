# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m,n = len(s), len(t)
        if m<n:
            return ""
        start, end =0,0
        t_dicts = {}
        for item in t:
            if t_dicts.get(item, 0) == 0:
                t_dicts[item] = 1
            else:
                t_dicts[item] += 1
        i = 0
        # j从一开始，使得对字符串切片时取得下标从i....j-1
        for j, item in enumerate(s, 1):
            if t_dicts.get(item, None) == None:
                t_dicts[item] = 0
            if t_dicts[item] > 0:
                n -= 1
            t_dicts[item] = t_dicts[item] - 1
            # 寻找字符串的起点位置
            if n == 0:
                # 恢复不是起点的下标的值
                while i < j and t_dicts[s[i]] < 0:
                    t_dicts[s[i]] += 1
                    i += 1
                # 更新窗口
                if end == 0 or j - i < end - start:
                    start, end = i, j
                # 舍弃窗口的第一个值
                t_dicts[s[i]] += 1
                n += 1
                i += 1
        return s[start: end]


if __name__ == '__main__':
    sol = Solution()
    s = "ADOBECODEBANC"
    t = "ABC"
    print(sol.minWindow(s,t))