class Solution(object):
    def subsets(self, nums):
        ans = [[]]
        for n in range(1,len(nums)+1):
            arr = list(map(list,list(itertools.combinations(nums, n))))
            ans+=arr
        return ans