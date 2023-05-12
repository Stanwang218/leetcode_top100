class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n = len(text1), len(text2)
        matrix = [[0 for i in range(n+1)] for j in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i - 1] == text2[j - 1]:
                    matrix[i][j] = matrix[i-1][j-1] + 1
                else:
                    matrix[i][j] = max(matrix[i][j-1], matrix[i-1][j])
        print(matrix)
        return matrix[m][n]


if __name__ == '__main__':
    s = Solution()
    lcm = s.longestCommonSubsequence("bsbininm","jmjkbkjkv")
    print(lcm)
        