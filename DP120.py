"""
DP
"""
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        
        
        n = len(triangle)
        
        dp =[[-1]*n]*n 
        
        def recur(triangle,idx,level,n,dp):
            if level==n:
                return
            
            dp[level][idx] = min(recur(triangle,idx,level+1,n,dp),recur(triangle,idx+1,level+1,n,dp))
            
            
        level = 1
        idx = 0
        recur(triangle,idx,level,n,dp)
        print(dp)
        return dp[level][idx]
        
        
        
        
        
        
        
        
