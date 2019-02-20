#include <iostream>
#include <string>
using namespace std;
class Solution {
public:
	int lengthOfLongestSubstring(string s) {
		int max = 0;
		string no_repeat = "";
		if(s.empty())
			return 0;
		for (int i = 0; i < s.size(); i++)
		{
			string no_repeat = "";
			for (int j = i; j < s.size(); j++)
			{
				no_repeat.push_back(s[j]);

				int flag = no_repeat.find(s[j + 1]);
				if (flag != -1)
				{
					max = max<=no_repeat.size()?no_repeat.size():max;
					break;
				}
				
			}

			max = max<=no_repeat.size()?no_repeat.size():max;
		}
		max = max<=no_repeat.size()?no_repeat.size():max;
		return max;
	}
	
};

int main() {
	string test = "ab";
	Solution s;
	int res = s.lengthOfLongestSubstring(test);
	cout<<res<<endl;
}