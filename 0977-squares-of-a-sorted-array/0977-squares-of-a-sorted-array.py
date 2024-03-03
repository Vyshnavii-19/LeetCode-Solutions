class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # nums.sort()
        arr=[i*i for i in nums]
        arr.sort()
        return arr