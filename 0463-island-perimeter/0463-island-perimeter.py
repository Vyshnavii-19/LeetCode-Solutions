class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        peri = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1: 
                    peri += 4
                    if row > 0 and grid[row-1][col] == 1: peri -= 2
                    if col > 0 and grid[row][col-1] == 1: peri -= 2
        
        return peri