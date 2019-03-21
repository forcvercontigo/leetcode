class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[-1 for _ in range(m)] for _ in range(n)]
        dp[0][0] = 1
        def recur(row,col,dp):
            if row == 0 or col == 0:
                return 1
            if dp[row][col] != -1:
                return dp[row][col]
            dp[row][col] = recur(row-1,col,dp)+recur(row,col-1,dp)
            return dp[row][col]
        return recur(n-1,m-1,dp)
        
        
        
        
        
        
        
