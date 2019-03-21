class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        n1 = len(word1)
        n2 = len(word2)
        i,j = 0,0
        dp = [[-1 for _ in range(n2)] for _ in range(n1)]
        def match(word1,word2,i,j,n1,n2):
            
            if i == n1:
                return n2-j
            if j == n2:
                return n1-i
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            if word1[i] == word2[j]:
                dp[i][j]= match(word1,word2,i+1,j+1,n1,n2)
            else:   
                dp[i][j] = min(min(match(word1,word2,i+1,j,n1,n2)\
                               ,match(word1,word2,i,j+1,n1,n2)),\
                           match(word1,word2,i+1,j+1,n1,n2))+1
           
            return dp[i][j]
        
        return match(word1,word2,0,0,n1,n2)
            
            
                
