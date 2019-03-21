class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if not n:
            return []
        
        d = [[0]*n for _ in range(n)]
        
        top, right, bottom, left = 0, n-1, n-1, 0
        
        count = 0
        while top < bottom and left < right:
            for i in range(left, right+1):
                count += 1
                d[top][i] = count
            top += 1
        
            for i in range(top, bottom+1):
                count += 1
                d[i][right] = count
            right -= 1
        
            for i in range(right, left-1, -1):
                count += 1
                d[bottom][i] = count
            bottom -= 1
        
            for i in range(bottom, top-1, -1):
                count += 1
                d[i][left] = count
            left += 1
            
        if n%2:
            d[n//2][n//2] = count + 1
        
        return d
