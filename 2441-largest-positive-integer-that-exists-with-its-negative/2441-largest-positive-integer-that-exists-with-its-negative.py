class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        maxx=-1
        for i in range(len(nums)):
            m=str(nums[i])
            
            if m[0]=="-":
                for j in range(i+1,len(nums)):
                    n = str(nums[j])
                    if n[0]!="-" and m[1:]==n:
                        maxx=max(maxx,int(m[1:]))
            else:
                for j in range(i+1,len(nums)):
                    n = str(nums[j])
                    if n[0]=="-" and n[1:]==m:
                        maxx=max(maxx,int(n[1:]))
                
        return maxx