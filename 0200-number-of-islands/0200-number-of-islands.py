class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def fun(grid,i,j):
            if grid[i][j]=='1':
                grid[i][j]='0'
            else:
                return
            if i<len(grid)-1:
                fun(grid,i+1,j)
            if i>0:
                fun(grid,i-1,j)
            if j<len(grid[0])-1:
                fun(grid,i,j+1)
            if j>0:
                fun(grid,i,j-1)
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    count+=1
                    fun(grid,i,j)
        return count