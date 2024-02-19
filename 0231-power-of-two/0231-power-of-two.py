class Solution:
    import math
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False

        x=math.log2(n)

        return x==int(x)
        