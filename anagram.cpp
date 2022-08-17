#include <algorithm>
#include <vector>
#include <iterator>
class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.size()!=t.size())
            return false;
        
        string work = s;
        
        std::sort(work.begin(),work.end());
        auto it = std::unique(work.begin(),work.end());
        work.resize(std::distance(work.begin(),it));
        std::vector<int> str1{},str2{};
        
        for(int i = 0; i < work.size(); i++){
            str1.push_back(std::count(s.begin(), s.end(), work[i]));
            str2.push_back(std::count(t.begin(), t.end(), work[i]));
        }
        
        if(str1!=str2)
            return false;
        
        for(int i = 0; i < s.size(); i++){
            if(t.find(s[i])==std::string::npos)
                return false;
        }
        return true;
    }
};