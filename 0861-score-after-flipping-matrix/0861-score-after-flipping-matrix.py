class Solution(object):
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        h = len(A)
        w = len(A[0])
        
        # if A[i][0] == 0, this row must be reversed
        for i in range(h):
            if A[i][0] == 0:
                for j in range(w):
                    A[i][j] = 1 - A[i][j]
        
        # if col's 0 more than 1, reverse this col.
        for j in range(1, w):
            col_sum = sum([A[i][j] for i in range(h)])
            if col_sum > h / 2:
                continue
            else:
                for i in range(h):
                    A[i][j] = 1 - A[i][j]
        
        # calculate the sum
        res = 0
        for i in range(h):
            cur = 0
            for j in range(w):
                cur <<= 1
                cur += A[i][j]
            res += cur
            

        return res