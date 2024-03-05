class Solution:
    def minimumLength(self, s: str) -> int:
        if len(s)==1:
            return 1
        start,end=0,len(s)-1
        while start<end and s[start]==s[end]:
            c=s[start]
            
            
            while start<=end and s[start]==c:
                start+=1
            while start<=end and s[end]==c:
                end-=1
            # start+=1
            # end-=1
          

        return len(s[start:end+1])