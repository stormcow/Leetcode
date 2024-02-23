#include <algorithm>
class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        std::vector<int> sorted = nums;
        std::sort(sorted.begin(),sorted.end());
        std::vector<int> answer(nums.size());
        for (int i = 0; i < nums.size(); i++) {
            for (int j = 0; j < nums.size(); j++) {
              if (nums[i] == sorted[j]) {
                if (j != 0 && (sorted[j] == sorted[j - 1]))
                  answer[i] =
                      std::distance(sorted.begin(),
                                    std::find(sorted.begin(), sorted.end(), sorted[j]));
                else
                  answer[i] = j;
              }
            }
          }
        return answer;
    }
};