class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n_cols = len(grid[0])
        best = [[0] * (n_cols + 1) for _ in range(n_cols + 1)]
        next_best = copy.deepcopy(best)
        for i in reversed(range(len(grid))):
            for left in range(min(i + 1, n_cols - 1)):
                for right in range(max(left + 1, n_cols - i - 1), n_cols):
                    next_best[left][right] = grid[i][left] + grid[i][right] + max(
                        best[left + i][right + j] for i in [-1, 0, 1] for j in [-1, 0, 1]
                        if left + i < right + j
                    )

            best, next_best = next_best, best 

        return best[0][n_cols - 1]