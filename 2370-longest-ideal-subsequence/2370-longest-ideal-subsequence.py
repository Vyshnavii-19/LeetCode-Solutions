class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        # Allocate space for an ASCII table up to 'z' (index = 122)
        # It allows us not to omit subtraction and 
        # checks for negative indices in ranges [i-k, i+k]
        ascii = [0] * 123
        for ch in s:
            i = ord(ch)
            ascii[i] = max(ascii[i - k:i + k + 1]) + 1
        # max for the whole list works a little bit faster than for [97:]
        return max(ascii)