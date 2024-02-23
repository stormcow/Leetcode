#include <algorithm>
#include <vector>
class Solution {
public:
    int numJewelsInStones(string jewels, string stones) {
        std::vector<int> vstones{};
        int num{};
        
        for(auto i:jewels)
            num+=std::count(stones.begin(),stones.end(),i);
        
        return num;
    }
};