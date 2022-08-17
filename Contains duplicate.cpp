#include <algorithm>
#include <iterator>
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        for(int i = 0; i < nums.size(); i++){
            auto iter = std::next(nums.begin(),i+1);
            if(std::find(iter, nums.end(), nums[i])!=nums.end())
                return true;
        }
        return false;
    }
};
