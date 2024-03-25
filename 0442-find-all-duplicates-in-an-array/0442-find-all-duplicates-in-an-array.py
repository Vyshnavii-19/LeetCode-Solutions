class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []
        d = set()
        for num in nums:
            if num not in d:
                d.add(num)
            else:
                output.append(num)
        return output