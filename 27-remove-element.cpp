#include <algorithm>
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        
        while(std::find(nums.begin(),nums.end(),val)!=nums.end()){
            int position = std::distance(nums.begin(),std::find(nums.begin(),nums.end(),val));
            nums.erase(nums.begin()+position);
        }

        return nums.size();
    }
};