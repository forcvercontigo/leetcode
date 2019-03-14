class Solution(object):
    def minPathSum(self, grid):
        m, n = len(grid)-1, len(grid[0])-1
        cache = [[-1 for _ in range(n+1)] for _ in range(m+1)]
        cache[0][0] = grid[0][0]

        def _help(rows, cols):
            if cache[rows][cols] == -1:
                cache[rows][cols] = min(_help(rows-1, cols) if rows > 0 else sys.maxint, \
                                                _help(rows, cols -1) if cols > 0 else sys.maxint) + grid[rows][cols]
            return cache[rows][cols]

        return _help(m,n)
