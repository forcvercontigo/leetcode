class Solution(object):
    def maxSubArray(self, nums):
        
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 
        summ = 0
        maxx = -sys.maxsize-1
        for i in xrange(len(nums)):
            if summ+nums[i]<nums[i]:
                summ = nums[i]
            else:
                summ+=nums[i]
            if summ>maxx:
                maxx = summ
        return maxx
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
