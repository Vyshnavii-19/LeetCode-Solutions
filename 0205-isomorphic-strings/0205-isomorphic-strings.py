class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        d = {}
        value_set = set()
        
        for index, letter in enumerate(s):
            try:
                if d[letter] != t[index]:
                    return False
            except KeyError:    
                d[letter] = t[index]
                if d[letter] in value_set:
                    return False
                value_set.add(d[letter])

        return True