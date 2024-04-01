class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # count = 0
        # index=len(s)-1
        # if s[-1]==" ":
        #     for j in range(len(s)-1,-1,-1):
        #         if s[j]==" ":
        #             continue
        #         else:
        #             index=j
        #             break
        # for i in range(index,-1,-1):

        #     if s[i] != " ":
        #         count+=1
        #     else:
        #         break
        # return count

        count = 0
        index=len(s)-1
        for i in range(index,-1,-1):
            if s[i]==" ":
                continue
            else:
                if s[i] != " ":
                    count+=1
                    if s[i]!=" " and s[i-1]==" ":
                        break
                else:
                    break
        return count