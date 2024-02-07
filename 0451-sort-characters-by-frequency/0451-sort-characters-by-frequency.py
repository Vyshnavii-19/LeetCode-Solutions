class Solution:
    def frequencySort(self, s: str) -> str:
        dic={}
        for i in s:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        
        x = sorted(dic.items(), key=lambda x:x[1],reverse=True)
       
        ans=""
        for i in x:
            ans+= i[0]*int(i[1])


        return ans
