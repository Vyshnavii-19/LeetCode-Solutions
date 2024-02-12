class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        y=set(nums)
        z=list(y)
        
        for i in range(len(z)):
            if nums.count(z[i])>len(nums)/2:
                return (z[i])