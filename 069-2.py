class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        if x < 4:
            return 1
        if x >= 3 and x <= 8:
            return 2
        if x>=9 and x<16:
            return 3
        maxx = int(x/2)
        s = 2
        left = 0
        right = 0
        i = 1
        while i < maxx:
            s = 2**i
            if s > x:
                right = i
                left = i - 1
                break
            i += 1
        for i in xrange(2**((left//2)-1),2**((right//2)+1)):\
            if (i+1)**2 > x:
                return i 
            
            
        
