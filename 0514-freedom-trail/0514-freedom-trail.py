class Solution:
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """
        n=len(ring)
        dic=collections.defaultdict(list)
        for i in range(n):
            dic[ring[i]].append(i)
        
        stack=[(0,0)]
        
        for x in key:
            n2=len(stack)
            for y in dic[x]:
                next_st=float("inf")
                for j in range(n2):
                    stp, pos=stack[j]
                    dist=abs(y-pos)
                    next_st=min(dist+stp,n-dist+stp,next_st)
                stack.append((next_st+1,y))
            stack=stack[n2:]
        stack.sort()
        return stack[0][0]