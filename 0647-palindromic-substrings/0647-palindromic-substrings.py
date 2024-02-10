class Solution:
    def countSubstrings(self, s: str) -> int:
        #(O(N^2)) --->TC
        dp={}
        count=0
        for i in range(len(s)-1):
            for j in range(i+1,len(s)+1):
                if s[i:j] in dp:
                    count+=1
                    continue
                else:
                    if s[i:j] == s[j - 1:i - 1 if i != 0 else None:-1]:
                        count += 1
                        dp[s[i:j]]=1

        return count+1