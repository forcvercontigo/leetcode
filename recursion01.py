#Reverse a string
#
#

def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        def recur(idx,s,n):
            if idx>n:
                return 
            s[:idx+1] = [s[idx]] + s[:idx]
            recur(idx+1,s,n)
        recur(1,s,len(s)-1)
