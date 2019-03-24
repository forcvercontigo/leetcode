class Solution(object):
    def numDecodings(self, s):
        if not s or s[0] == '0':
            return 0
        c1 = 1
        c2 = 1
        
        for i in xrange(1,len(s)):
            if s[i] == '0':
                c1 = 0 
            
            if s[i-1] == '1' or s[i-1] == '2' and s[i] <='6':
                c1 += c2
                c2 = c1 - c2
            else:
                c2 = c1
        
        
        
        
        
        
        
        
