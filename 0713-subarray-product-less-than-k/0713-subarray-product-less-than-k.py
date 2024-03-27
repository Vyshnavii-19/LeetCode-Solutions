class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        counter = 0
        if k <= 1:
            return counter

        i1, prod = 0, 1
        for i2,value in enumerate(nums):
            prod *= value

            while prod >= k:
                prod /= nums[i1]
                i1 += 1

            counter += i2 - i1 + 1

        return counter