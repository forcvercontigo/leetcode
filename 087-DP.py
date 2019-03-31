# DP 
def isScramble1(self, s1, s2):
    if len(s1) != len(s2):
        return False
    if s1 == s2:
        return True
    if sorted(s1) != sorted(s2): # prunning
        return False
    for i in xrange(1, len(s1)):
        if (self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:])) or \
        (self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i])):
            return True
    return False
    
# DP with memorization
def __init__(self):
    self.dic = {}
    
def isScramble(self, s1, s2):
    if (s1, s2) in self.dic:
        return self.dic[(s1, s2)]
    if len(s1) != len(s2) or sorted(s1) != sorted(s2): # prunning
        self.dic[(s1, s2)] = False
        return False
    if s1 == s2:
        self.dic[(s1, s2)] = True
        return True
    for i in xrange(1, len(s1)):
        if (self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:])) or \
        (self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i])):
            return True
    self.dic[(s1, s2)] = False
    return False
