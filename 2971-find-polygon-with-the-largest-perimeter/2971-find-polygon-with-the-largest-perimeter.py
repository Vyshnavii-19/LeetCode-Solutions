class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        
        while 1:
            if not nums: return -1
            
            maxx = max(nums)
            suma = sum(nums) - maxx
            
            if suma<=maxx: nums.remove(maxx)
            else: break
                
                
        return sum(nums)
                
        
        