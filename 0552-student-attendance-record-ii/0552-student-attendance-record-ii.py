class Solution(object):
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        mod = 1000000007        
        def mul(a, b):
            n, m, l = len(a), len(b[0]), len(a[0])
            return [[sum([a[i][k] * b[k][j] for k in range(l)]) % mod for j in range(m)] for i in range(n)]
        
        B = [[1, 1, 1, 0, 0 ,0],
             [1, 0, 0, 0, 0 ,0],
             [0, 1, 0, 0, 0 ,0],
             [1, 1, 1, 1, 1 ,1],
             [0, 0, 0, 1, 0 ,0],
             [0, 0, 0, 0, 1 ,0]]
        
        f = [[1], [0], [0], [0], [0], [0]]
        
        Bn = B
        while n > 0:
            if n & 1:
                f = mul(Bn, f)
            n = n >> 1
            Bn = mul(Bn, Bn)
                
        return mul([[1, 1, 1, 1, 1, 1]], f)[0][0]