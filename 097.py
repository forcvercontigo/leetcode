class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s3) != len(s1) + len(s2):
            return False
        
        def isInterleaveInternal(i, j):
            if i == -1:
                return s3[:j + 1] == s2[: j + 1]
            if j == -1:
                return s3[:i + 1] == s1[: i + 1]
            if s3[i + j + 1] == s1[i] and isInterleaveMemo(i - 1, j):
                return True
            if s3[i + j + 1] == s2[j] and isInterleaveMemo(i, j - 1):
                return True
            return False
         
        def isInterleaveMemo(i, j):
            if not (i, j) in memo:
                memo[(i, j)] = isInterleaveInternal(i, j)
            return memo[(i, j)]
        
        memo = {}
        return isInterleaveMemo(len(s1) - 1, len(s2) - 1)
