class Solution:
    def pivotInteger(self, n: int) -> int:

        for i in range(1,n+1):
                
            k=1
            l=n
            temp1=0
            temp2=0
            x=i
     
            while k!=x:
                temp1+=k
                k+=1   
            while l!=x:
                temp2+=l
                l-=1
            if temp1-x==temp2-x:
                return i

        if n==1:
            return 1
        return -1

