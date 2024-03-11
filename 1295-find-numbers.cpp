class Solution {
public:
    int findNumbers(vector<int>& nums) {
        int evens{};
        for(int x: nums){
            int digits{1};
            while(x>=10){
                x=x/10;
                digits++;
            }
            if(digits%2==0 && digits!=0)
                evens++;
        }
        return evens;
    }
};