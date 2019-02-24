    def longestCommonPrefix(self, strs: 'List[str]') -> 'str':
        if len(strs) < 1:
            return ''
        if len(strs) == 1:
            return strs[0]
        prefix = ''
        idx = 0
        valid = True
        while valid:
            if len(strs[0]) > idx:
                letter = strs[0][idx]
                for word in strs:
                    if len(word) <= idx or word[idx] != letter:
                        valid = False
                        break
                if valid:
                    prefix += letter
                    idx += 1
            else:
                valid = False
        return prefix 
 #按列比较
 #只关注变化的时刻即可
 #用flag来标志是否为prefix
 #
 #
 #
 #
 #
 #
 #
 
