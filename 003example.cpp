

    int lengthOfLongestSubstring(string s){
    	vector<int> hash(256, -1);
    	int maxlen = 0;
    	int start = 0;
    	for (int i= 0; i< s.size(); ++i) {
    		if (hash[s[i]] != -1) {
    			start = max(start, hash[s[i]] + 1);
    		}
    		maxlen = max(maxlen, i- start + 1);
    		hash[s[i]] = i;
    	}
    	return maxlen;
    }
