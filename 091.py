class Solution(object):
    def numDecodings(self, s):
        if not s or s[0] == '0':
            return 0
        f = [1] + [0] * len(s)
        for i in xrange(1,len(s)+1):
            if s[i-1] != '0':
                f[i] += f[i-1]
            if i > 1 and '09' < s[i-2] + s[i-1] < '27':
                f[i] += f[i-2]
        return f[-1]
