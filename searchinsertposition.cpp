#include <algorithm>
class Solution {
public:
    
    int searchInsert(vector<int>& nums, int target) {
        std::vector<int>::iterator iter = std::find(nums.begin(),nums.end(),target);
        if(iter!=nums.end())
            return std::distance(nums.begin(),iter);
        else
        {
            nums.push_back(target);
            std::sort(nums.begin(),nums.end());
            std::vector<int>::iterator iter = std::find(nums.begin(),nums.end(),target);
            return std::distance(nums.begin(),iter);
        }
    }
};