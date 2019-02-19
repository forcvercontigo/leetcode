#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
//`ctrl+alt+f`: Format current file
class Solution {
public:
	vector<int> twoSum(vector<int>& nums, int target)
	{
		std::vector<int> res;
		vector<int>::iterator v = nums.begin();
		for (; v != nums.end(); v++)
		{
			std::vector<int>::iterator p = v + 1;
			for (; p != nums.end(); p++)
			{
				cout << *p << endl;
				if (*p + *v == target)
				{

					res.push_back(v - nums.begin());
					res.push_back(p - nums.begin());
				}
			}
		}
		return res;
	}

};
int main() {
	int a[4] = {2, 7, 11, 15};
	vector<int> nums(a, a + 4);
	int target = 9;
	Solution s;
	std::vector<int> res;
	res = s.twoSum(nums, target);
	cout << res[0] << '\t';
	cout << res[1] << endl;
}