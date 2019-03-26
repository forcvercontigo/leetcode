class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not t or not s or len(s)<len(t):
            return ''
        if t == s:
            return s
        l,r = 0,1
        size = len(s)
        res = ''
        s = s.strip()
        t = t.strip()
        t = list(t)
        t.sort()
        def valid(l,r):
            length = r - l
            tmp = list(s[l:r])
            count = 0
            for i in t:
                if i in tmp:
                    tmp.remove(i)
                else:
                    return False
            return True
        while r <= len(s) :
            #print(l,r,res)
            if r - l < len(t):
                r += 1
            else:
                if valid(l,r):
                    if r - l <= size:
                        res = s[l:r]
                        size = r -l
                    l += 1
                else:
                    r += 1
        return res
        
        
        
        
        
        
        
        
        
        
        
        
