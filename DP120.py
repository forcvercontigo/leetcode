class Solution:
    def helper(self, triangle, row, col, dest, memo):
        if row == dest:
            return triangle[row][col]
        
        if (row, col) in memo:
            return memo[(row, col)]
        
        min_sum = min(self.helper(triangle, row + 1, col, dest, memo), self.helper(triangle, row + 1, col + 1, dest, memo))
        
        memo[(row, col)] = min_sum + triangle[row][col]
        return memo[(row, col)]
    
    
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        subproblems:
        row_index, col_index -> end
        """
        if not triangle:
            return 0
        
        dest = len(triangle) - 1
        return self.helper(triangle, 0, 0, dest, {})
