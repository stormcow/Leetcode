class Solution {
public:
    vector<int> createTargetArray(vector<int>& nums, vector<int>& index) {
        vector<int> ans(nums.size());
        
        for(int i = 0; i < nums.size(); i++){
            ans.insert(ans.begin()+index[i],nums[i]);
        }
        
        ans.resize(nums.size());
        
        return ans;
    }
};