class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int ones{};
        int current{};
        for(int x:nums){
            if(x==1){
                current++;
            }
            else{
                if(current>ones)
                    ones=current;
                current=0;
            }
        }
        if(current>ones)
                    ones=current;
        return ones;
    }
};