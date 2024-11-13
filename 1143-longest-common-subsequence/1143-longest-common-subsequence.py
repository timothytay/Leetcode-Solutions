class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * len(text1) for _ in range(len(text2))]
        # cols are str1 and rows are str2 

        
        rows = len(text2)
        cols = len(text1)
        for r in range(len(text2) - 1, -1, -1):
            for c in range(len(text1) - 1, -1, -1):
                if text1[c] == text2[r]:
                    dp[r][c] = 1 + (dp[r+1][c+1] if r + 1 < rows and c + 1 < cols else 0)
                else:
                    dp[r][c] = max(dp[r+1][c] if r + 1 < rows else 0, dp[r][c+1] if c + 1 < cols else 0)
        return dp[0][0]
