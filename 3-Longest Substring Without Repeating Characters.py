class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        ans = 1
        sets = set()
        l, r = 0, -1
        # substring = s[l] .... s[r] 
        # l indicates the left index of the element
        # r indicates the right index of the element
        # l,r代表窗口左右两个值的下标
        for item in s: 
            r += 1
            # if current element is not in the set, add it into the set
            # 如果当前元素不在集合中，加入
            if item not in sets:
                sets.add(item)
                ans = max(r - l + 1, ans)
            # if current is in the set, move the left index until the left element is the right element
            # 关闭窗口，直到左侧元素和右侧元素相同
            else:
                while l < r and s[l] != item:
                    sets.remove(s[l])
                    l += 1
                l += 1
        return ans

if __name__ == '__main__':
    s = Solution()
    string = "pwwke"
    string = "pwcwke"
    # string = "abcabcbb"
    print(s.lengthOfLongestSubstring(string))