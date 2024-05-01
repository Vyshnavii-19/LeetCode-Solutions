class Solution:
    def tribonacci(self, n: int) -> int:
        dp=[0]*41
        dp[0]=0
        dp[1]=1
        dp[2]=1
        for i in range(n):
            dp[i+3]=dp[i]+dp[i+1]+dp[i+2]
        return dp[n]