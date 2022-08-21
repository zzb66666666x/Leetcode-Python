# https://leetcode.com/problems/decode-ways/
class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 1:
            return 1 if s[0] != '0' else 0
        dp = [0 for i in range(len(s)+1)]
        dp[0] = 1 
        dp[1] = 1 if s[0] != '0' else 0
        for i in range(2, len(s)+1):
            curchar = s[i-1]
            prevchar = s[i-2]
            if prevchar == '0' or prevchar+curchar > '26':
                dp[i] = dp[i-1] if curchar != '0' else 0
            else:
                dp[i] = dp[i-1] + dp[i-2] if curchar != '0' else dp[i-2]
        # print(dp)
        return dp[-1]
            
            
