class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 
        
        res = triangle[-1]
        for i in xrange(len(triangle)-2, -1, -1):
            for j in xrange(len(triangle[i])):# j is range from 0 to len(upper level ,so it can not be overflow)
                print(res)
                print(i,j)
                res[j] = min(res[j], res[j+1]) + triangle[i][j]
                
        return res[0]
