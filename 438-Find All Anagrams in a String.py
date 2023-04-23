# Input: s = "cbaebabacd", p = "abc"
# Output: [0, 6]

class Solution:
    def findAnagrams(self, s: str, p: str) -> list:
        ans = []
        m, n = len(s), len(p)
        p_dict = {}
        for item in p:
            if p_dict.get(item, 0) == 0:
                p_dict[item] = 1
            else:
                p_dict[item] += 1
        i, j = 0, 0
        flag = False
        while j < m:
            # 右侧窗口在字典中
            if s[j] in p_dict:
                # 如果窗口右侧已经为零，移动左侧
                if p_dict[s[j]] == 0:
                    while p_dict[s[j]] <= 0:
                        p_dict[s[i]] += 1
                        i += 1
                        n += 1
                p_dict[s[j]] -= 1
                n -= 1
                if not flag:
                    i = j
                flag = True
            else:
                # 关闭窗口
                for index in range(i, j+1):
                    if s[index] in p_dict:
                        p_dict[s[index]] += 1
                        n += 1
                flag = False
                i = j
            # 如果找到一个合适的起点
            if n == 0:
                ans.append(i)
                # 缩小左侧窗口
                p_dict[s[i]] += 1
                i += 1
                n += 1
            j += 1  
        return ans

if __name__ == '__main__':
    sol = Solution()
    s = "abcdab"
    p = "ab"
    s = "eklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsn"
    p = "yqrbgjdwtcaxzsnifvhmou"
    print(sol.findAnagrams(s,p))