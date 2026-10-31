class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        # right[i][j] = ways to reach (i, j) while moving right
        # down[i][j]  = ways to reach (i, j) while moving down
        right = [[0] * n for _ in range(m)]
        down = [[0] * n for _ in range(m)]
        right[0][0] = 1  # start (direction doesn't matter, cell is empty)

        for i in range(m):
            for j in range(n):
                r, d = right[i][j], down[i][j]
                if r == 0 and d == 0:
                    continue
                if grid[i][j] == 1:
                    # entered moving right -> turned down
                    if r and i + 1 < m:
                        down[i + 1][j] = (down[i + 1][j] + r) % MOD
                    # entered moving down -> turned right
                    if d and j + 1 < n:
                        right[i][j + 1] = (right[i][j + 1] + d) % MOD
                else:
                    total = (r + d) % MOD
                    if j + 1 < n:
                        right[i][j + 1] = (right[i][j + 1] + total) % MOD
                    if i + 1 < m:
                        down[i + 1][j] = (down[i + 1][j] + total) % MOD

        return (right[m - 1][n - 1] + down[m - 1][n - 1]) % MOD
