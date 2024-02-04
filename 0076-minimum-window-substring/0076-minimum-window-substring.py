class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ''

        res,resLen = [-1,-1],math.inf
        countT = Counter(t)
        have,need = 0,len(countT)
        window = {}
        l=0

        for r,c in enumerate(s):
            window[c] = window.get(c,0)+1

            if countT[c]==window[c]:
                have+=1

                while have==need:
                    if r-l+1<resLen:
                        res = [l,r]
                        resLen = r-l+1
                    
                    window[s[l]]-=1
                    if countT[s[l]]>window[s[l]]:
                        have-=1
                    l+=1

        return '' if resLen==math.inf else s[res[0]:res[1]+1]



