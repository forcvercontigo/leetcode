from collections import Counter
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        #firstly handle exception
        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]
        #compute the minimum length of all items 
        min_len = len(strs[0])
        lt = []
        for i in strs:
            if len(i)<min_len:
                min_len = len(i)
         # for every item in strs,save the first j characters
        for i in strs:
            for j in range(min_len):
                lt.append(i[0:j+1])
        #calculate the times these strings showing,return is dictionary
        count = Counter(lt)
        max_len = 0
        lt_key = []
        #if the string showing in every item in strs,add it into list
        for key,values in count.items():
            if values == len(strs):
                lt_key.append(key)
        key = ''
        #find the longest string as return value
        for i in lt_key:
            if max_len < len(i):
                max_len = len(i)
                key = i
        return key
