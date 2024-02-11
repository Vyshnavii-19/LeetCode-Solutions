class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        elif len(grid[0]) == 1:
            return grid[0][0] + grid[0][-1]
        
        dirs = [(0,0),(0,1),(0,-1),(1,0),(1,1),(1,-1),(-1,0),(-1,1),(-1,-1)]
        
        M, N = len(grid), len(grid[0])
        
        old = [[0 for _ in range(N+2)] for _ in range(N+2)]
        
        
        engrid = [[0 for _ in range(N+2)] for _ in range(M)]
        for i in range(M):
            for j in range(1, N+1):
                engrid[i][j] = grid[i][j-1]
        
        old[1][N] = grid[0][0] + grid[0][-1]

        tmp = [[0 for _ in range(N+2)]  for _ in range(N+2)]
        for i in range(M-1):
            new = [[0 for _ in range(N+2)] for _ in range(N+2)]
            for j1 in range(1, N+1):
                for j2 in range(1, N+1):
                    if old[j1][j2] or (i == 0 and grid[0][0] + grid[0][-1] == 0):
                        for d1, d2 in dirs:
                            nxt_j1, nxt_j2 = j1 + d1, j2 + d2
                            if nxt_j1 == 0 or nxt_j2 == N+1 or nxt_j2 == 0 or nxt_j1 == N+1:
                                continue
                            tmp = engrid[i+1][nxt_j1] + engrid[i+1][nxt_j2] if nxt_j1 != nxt_j2 else engrid[i+1][nxt_j1]
                            new[nxt_j1][nxt_j2] = max(new[nxt_j1][nxt_j2], old[j1][j2] + tmp)
            old = new
                        
        res = 0
        for j1 in range(1, N+1):
            res = max(res, max(old[j1]))
        return res