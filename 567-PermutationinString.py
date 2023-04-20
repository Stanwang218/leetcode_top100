# Input:"ab"
# Output: "eidbaooo"

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m,n = len(s1), len(s2)
        if m > n:
            return False
        s1_dicts = {}
        for item in s1:
            if item in s1_dicts:
                s1_dicts[item] += 1
            else:
                s1_dicts[item] = 1
        i = 0
        j = 0
        flag = False # have a window ?
        while j < n:
            # 如果当前字符不属于匹配字符 关闭窗口
            if s2[j] not in s1_dicts:
                if flag:
                    for index in range(i, j):
                        if s2[index] in s1_dicts:
                            s1_dicts[s2[index]] += 1
                            m += 1
                flag = False
            else:
                # 标记窗口的起始位置
                if not flag:
                    i = j
                    flag = True
                # 如果当前字符已经在之前访问过，缩小窗口
                while s1_dicts[s2[j]] <= 0:
                    s1_dicts[s2[i]] += 1
                    i += 1
                    m += 1
                # 扩大窗口
                if s1_dicts[s2[j]] > 0:
                    s1_dicts[s2[j]] -= 1
                    m -= 1
                    if m == 0:
                        return True
            j += 1
        return False


if __name__ == '__main__':
    sol = Solution()
    s1 = "ab"
    s2 = "eidbaooo"
    # s1 = "hello"
    # s2 = "ooolleoooleh"
    # s1 = "ky"
    # s2 = "ainwkckifykxlribaypk"
    print(sol.checkInclusion(s1,s2))