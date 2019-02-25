class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        res = []
        if len(digits)==0:
            return res
        def dfs(num,string,res):
            if num == end:
                res.append(string)
                return
            else:
                for letter in dic[int(digits[num])]:
                    dfs(num+1,string+letter,res) 
        dic = {2:['a','b','c'],3:['d','e','f'],4:['g','h','i'],5:['j','k','l'],6:['m','n','o'],\
               7:['p','q','r','s'],8:['t','u','v'],9:['w','x','y','z']}
        end = len(digits)
        dfs(0,'',res)
        return res
