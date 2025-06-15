class Solution:
    def countSubstrings(self, s: str) -> int:
        
        count = 0
        dp = [[False] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
            count += 1
        for i in range(len(s) - 1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                count += 1
        for i in range(3, len(s) + 1):
            if i % 2:
                half = i // 2
                for j in range(len(s)):
                    if (j - half >= 0 and j + half < len(s) and s[j - half] == s[j + half] and dp[j - half + 1][j + half - 1]):
                        dp[j - half][j + half] = True
                        count += 1
            else:
                half = i // 2 - 1
                for j in range(len(s)):
                    if (j - half >= 0 and j + 1 + half < len(s) and s[j - half] == s[j + 1 + half] and dp[j - half + 1][j + 1 + half - 1]):
                        dp[j - half][j + 1 + half] = True
                        count += 1




        return count
        
