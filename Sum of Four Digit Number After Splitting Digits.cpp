#include <vector>
#include <string>
#include <algorithm>
class Solution {
public:
    int minimumSum(int num) {
        int sum{};
        std::string num1{}, num2{};
        std::vector<int> vec{};
        std::string sub = std::to_string(num);
        for(auto i:sub){
            vec.push_back((int)i-'0');
        }
        std::sort(vec.begin(),vec.end());
        
        num1+=std::to_string(vec[0]);
        num1+=std::to_string(vec[2]);
        num2+=std::to_string(vec[1]);
        num2+=std::to_string(vec[3]);
        
        sum = (std::stoi(num1))+(std::stoi(num2));
        return sum;
    }
};