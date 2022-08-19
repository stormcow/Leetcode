#include <algorithm>
class Solution {
  public:
    vector<int> twoSum(vector<int>& nums, int target){
        int x{},y{},current{};
        for(int i = 0; i < nums.size() - 1; i++){
            x = i;
            current = target;
            current -=nums[i];
            auto iter =std::find(nums.begin()+i+1,nums.end(), current); 
            if(iter!=nums.end())
            {
                y = std::distance(nums.begin(),iter);
                break;
            }
            
        }
        return vector<int>{x,y};
    }
};