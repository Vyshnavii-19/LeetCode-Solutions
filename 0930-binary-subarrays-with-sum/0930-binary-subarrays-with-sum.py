class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        res = 0
        ones = [-1]
        for i, x in enumerate(A):
            if x == 1:
                ones.append(i)
        ones.append(len(A))
        if S == 0:
            return sum([(ones[i]-ones[i-1])*(ones[i]-ones[i-1]-1)//2 for i in range(1, len(ones))])
        if len(ones)-2 < S:
            return 0
        for i in range(1, len(ones)-S):
            res += (ones[i]-ones[i-1]) * (ones[i+S]-ones[i+S-1])
        return res