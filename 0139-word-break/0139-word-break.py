class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)

        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if word == s[i:] or (i + len(word) <= len(s) and word == s[i:i+len(word)] and dp[i+len(word)]):
                    dp[i] = True
        return dp[0]