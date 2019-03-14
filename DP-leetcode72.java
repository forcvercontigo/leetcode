public class Solution {
    /**
     * Recursive solution.
     * For each poisition, check three subproblem:
     * 1. insert
     * 2. delete
     * 3. replace
     * We only modify the first string since no matter which one we choose, the result is the same. 
     * Got TLE since we recursively solve the same subproblem several times.
     * Appromixately O(len1 ^ 3) time in the worst case.
     * Need to optimize it using cache, which is the idea of dynamic programming. 
     * The key point is to find out the subproblem we have solved duplicately and cache the recursion.
     * Noticed that each subproblem is specificed by i and j pointer, so we can cache the result of these subproblems. 
     */
    public int minDistance(String word1, String word2) {
        if (word1 == null || word1.length() == 0) return word2.length();
        if (word2 == null || word2.length() == 0) return word1.length();
        
        return match(word1, word2, 0, 0);
    }
    
    private int match(String s1, String s2, int i, int j) {
        //If one of the string's pointer have reached the end of it
        if (s1.length() == i) {
            return s2.length() - j;
        }
        if (s2.length() == j) {
            return s1.length() - i;
        }
        
        int res;
        //If current poisition is the same.
        if (s1.charAt(i) == s2.charAt(j)) {
            res = match(s1, s2, i + 1, j + 1);
        } else {
            //Case1: insert
            int insert = match(s1, s2, i, j + 1);
            //Case2: delete
            int delete = match(s1, s2, i + 1, j);
            //Case3: replace
            int replace = match(s1, s2, i + 1, j + 1);
            res = Math.min(Math.min(insert, delete), replace) + 1;
        }
        
        return res;
    }
}  
