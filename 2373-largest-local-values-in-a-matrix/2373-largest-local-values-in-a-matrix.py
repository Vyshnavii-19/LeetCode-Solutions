class Solution:
	def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:

		result = [[0  for _ in range(len(grid)-2)] for _ in range(len(grid)-2)]

		def get_max_value(r,c):

			max_value = max( grid[r][c : c + 3] + grid[r + 1][ c : c + 3] + grid[r + 2][c : c + 3])

			return max_value

		for row in range(len(grid)-2):

			for col in range(len(grid)-2):

				result[row][col] = get_max_value(row, col)

		return result