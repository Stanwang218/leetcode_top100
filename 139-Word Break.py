def wordBreak(s, wordDict):
    n = len(s)
    dp = [False for i in range(n+1)]
    dp[0] = True
    for i in range(1,n +1):
        for word in wordDict:
            if i - len(word) < 0:
                continue
            if dp[i-len(word)] and s[i - len(word): i] == word:
                dp[i] = True
    return dp[n]

if __name__ == '__main__':
    s = "a"
    wordDict = ["aa","aaa"]
    b = wordBreak(s, wordDict)
    print(b)
    print(s[-2])