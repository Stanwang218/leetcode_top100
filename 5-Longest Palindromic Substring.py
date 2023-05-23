# Input: s = "babad"
# Output: "bab"

# dp version
def dp_longestPalindrome(s: str) -> str:
    n = len(s)
    dp = [[0] * n for i in range(n)]
    max_l, max_r = 0,0
    for i in range(n):
        dp[i][i] = 1
    for i in range(n, -1, -1):
        for j in range(i + 1,n):
            if s[i] == s[j]:
                if j - i == 1 or dp[i+1][j-1]:
                    dp[i][j] = 1
                    if j - i + 1 > max_r - max_l + 1:
                        max_l, max_r = i, j
    return s[max_l: max_r + 1]

# two pointer version
def tp_longestPalindrome(s: str) -> str:
    n = len(s)
    max_l, max_r = 0,0
    for i in range(n):
        left, right = i,i
        while right < n and s[left] == s[right]:
            right += 1
        left = left - 1

        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1

        temp_len = right - left - 1
        if temp_len > max_r - max_l + 1:
            max_l,max_r = left+1,right-1

    return s[max_l: max_r + 1]

if __name__ == '__main__':
    s = "aaaa"
    print(tp_longestPalindrome(s))