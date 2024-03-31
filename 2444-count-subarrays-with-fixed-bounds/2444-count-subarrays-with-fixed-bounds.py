class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        i_min = -1
        i_max = -1
        last_ok = -1
        last_bad = -1
        cnt = 0
        for i, x in enumerate(nums):
            if x < minK or x > maxK:
                last_bad = i
            else:
                if x == minK:
                    i_min = i
                    last_ok = i_max
                if x == maxK:
                    i_max = i
                    last_ok = i_min
                diff = last_ok - last_bad
                if diff > 0:
                    cnt += diff
        return cnt