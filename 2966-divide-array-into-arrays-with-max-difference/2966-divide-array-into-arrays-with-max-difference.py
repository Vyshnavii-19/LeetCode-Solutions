class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        ans=[]
        nums.sort()
        for i in range(len(nums)):
            if i%3==0:
                if abs(nums[i]-nums[i+1])<=k and abs(nums[i+1]-nums[i+2])<=k and abs(nums[i]-nums[i+2])<=k:

                    ans.append(nums[i:i+3])
          
        # return ans
        # ans=[]
        # already=[]
        # nums.sort()
        # if len(nums)%3!=0:
        #     return []
        # for i in range(len(nums)-2):
        #     first=nums[i]
        #     for j in range(i+1,len(nums)-1):
        #         second=nums[j]
        #         for m in range(j+1,len(nums)):
        #             third=nums[m]
        #             if abs(first-second)<=k and abs(second-third)<=k and abs(first-third)<=k:

        #                 if i not in already :
        #                     if j not in already:
        #                         if m not in already:
        #                             already.append(i)
        #                             already.append(j)
        #                             already.append(m)

        #                             ans.append([first,second,third])
        # print(ans)      
     
        if len(ans)!= len(nums)//3:
            return []
                   
        return ans
        