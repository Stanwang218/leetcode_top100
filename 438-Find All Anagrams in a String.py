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
            print(s[j])
            if s[j] in p_dict:
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
                for index in range(i, j+1):
                    if s[index] in p_dict:
                        p_dict[s[index]] += 1
                        n += 1
                flag = False
                i = j
            if n == 0:
                ans.append(i)
                p_dict[s[i]] += 1
                i += 1
                n += 1
                # flag = False
            j += 1  
        return ans

if __name__ == '__main__':
    sol = Solution()
    s = "abcdab"
    p = "ab"
    s = "eklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsn"
    p = "yqrbgjdwtcaxzsnifvhmou"
    print(sol.findAnagrams(s,p))