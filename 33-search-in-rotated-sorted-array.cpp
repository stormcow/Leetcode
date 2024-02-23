#include <algorithm>

class Solution {
public:
    int search(vector<int>& nums, int target) {
        auto result = std::find(nums.begin(),nums.end(),target);
        
        if (result == nums.end())
            return -1;
        else
            return std::distance(nums.begin(), result);
    }
};
