#include <algorithm>
class Solution {
   void prefix(std::vector<std::string>& strs, std::string& answer) {
    std::sort(strs.begin(), strs.end(), []
    (const std::string& first, const std::string& second) {
            return first.size() < second.size();
        });
    std::string sub = strs[0];
    std::string current{};
    for (int j = 0; j < strs[0].size(); j++) {
        if (sub.size() == 0)
            return;
        for (int i = 0; i < strs.size(); i++)
        {
            if (sub == strs[i].substr(0, sub.size()))
            {
                current = sub;
            }
            else {
                current = "";
                sub.pop_back();
                break;
            }
        }
        if (current.size() > answer.size())
            answer = current;
    }

}
    public:
    string longestCommonPrefix(vector<string>& strs) {
        string answer{};
        prefix(strs,answer);
        return answer;
    }
};