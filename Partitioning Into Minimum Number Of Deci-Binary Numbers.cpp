#include <string>
class Solution {
public:
    int minPartitions(string n) {
        int max{};
        
        for(auto i:n){
            if(max<((int)i-'0'))
                max=((int)i-'0');
        }
        
        return max;
    }
}