class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        p=list(set(nums))
        k=[]
        count=0
        for i in p:
            k.append(nums.count(i))
        x=max(k)
        for i in range(len(k)):
            if x==k[i]:
                count+=x
        return count

