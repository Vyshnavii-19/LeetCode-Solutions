class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not str:
            return True
        opening_brackets = []
        closing_brackets = []
        stars = []
        for i, letter in enumerate(s):
            if letter == '(':
                opening_brackets.append(i)
            elif letter == ')':
                if opening_brackets:
                    opening_brackets.pop()
                else:
                    closing_brackets.append(i)
            else: 
                stars.append(i)
        if len(opening_brackets) + len(closing_brackets) > len(stars):
            return False
        if opening_brackets:
            for bracket in opening_brackets:
                index = 0
                n = len(stars)
                while index < n and stars[index] <= bracket:
                    index += 1
                if index >= n:
                    return False
                else:
                    stars.remove(stars[index])
        if closing_brackets:
            for bracket in closing_brackets:       
                n = len(stars)
                index = n-1
                while index >= 0 and stars[index] >= bracket:
                    index -= 1
                if index < 0:
                    return False
                else:
                    stars.remove(stars[index])
        return True