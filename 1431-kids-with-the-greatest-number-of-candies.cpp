#include <algorithm>
class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        std::vector<bool> result{};
        
        for(int i = 0; i < candies.size(); i++){
            candies[i] +=extraCandies;
            if(candies[std::distance(candies.begin(), std::max_element(candies.begin(),candies.end()))]==candies[i])
                result.push_back(true);
            else
                result.push_back(false);
            candies[i]-=extraCandies;
        }
        
        return result;
    }
};