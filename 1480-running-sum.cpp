class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        vector<int> sum{};
        int num{};
        for(int i = 0; i < nums.size(); i++){             
            
            sum.push_back(nums[i]+num);
            num+=nums[i];
        }
        return sum;
    }
};