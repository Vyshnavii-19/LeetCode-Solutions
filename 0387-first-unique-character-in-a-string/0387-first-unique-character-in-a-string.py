class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in s:
            if s.rindex(i)==s.index(i):
                return s.index(i)
        return -1