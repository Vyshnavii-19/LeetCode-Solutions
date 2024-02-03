class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0]*(n+1)
        for i in range(n):
            curMax = curSum = 0
            for j in range(i, max(-1, i-k), -1):
                if curMax < arr[j]:
                    curMax = arr[j]
                cur = curMax*(i-j+1)+dp[j]
                if curSum < cur:
                    curSum = cur
            dp[i+1] = curSum
        return dp[-1]