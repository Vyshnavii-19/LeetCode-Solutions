class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        dicc={}
        dicc2={}
        for i in trust:
            if i[-1] in dicc:
                dicc[i[-1]]+=1
            else:
                dicc[i[-1]]=1
        for j in trust:
            if j[0] in dicc:
                dicc2[j[0]]=True
        for i in range(1,n+1):
            if i not in dicc2:
                if i in dicc:
                    if dicc[i]==n-1:

                        return i
        if n==1:
            return 1   
        return -1