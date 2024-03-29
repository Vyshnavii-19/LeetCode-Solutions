class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans, lar, n = 0, max(nums), len(nums)
        ind = []
        for i in range(len(nums)):
            if nums[i] == lar:
                ind.append(i)
        ind.append(n)
        ans = 0
        for i in range(0,len(ind) - k):
            ans+=(ind[i]+1)*(ind[i+k]-ind[i+k-1])
        return ans
        