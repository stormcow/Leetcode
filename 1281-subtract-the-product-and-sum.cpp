#include <string>
class Solution {
public:
    int subtractProductAndSum(int n) {
        
        std::string str = std::to_string(n);
        
        int product{1};
        int sum{};
        
        for(auto i:str){
            int num = (int)i-'0';
            product*=num;
            sum+=num;
        }
        
        return product-sum ;
        
    }
};