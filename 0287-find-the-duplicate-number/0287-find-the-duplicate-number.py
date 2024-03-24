class Solution:
    def findDuplicate(self, nums):
        start = 1
        end = len(nums) - 1
        while start < end:
            mid = start + (end - start) // 2
            count = self.getCount(nums, start, mid)
            if count <= (mid - start + 1):
                start = mid + 1
            else:
                end = mid
        return start

    def getCount(self, nums, start, end):
        count = 0
        for num in nums:
            if start <= num <= end:
                count += 1
        return count