class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        std::string substring{};
        int max{};
        
        for(int i = 0; i < s.size(); i++){
            if (substring.find(s[i]) == std::string::npos)
      substring += s[i];
    else {
      if (substring.size() > max)
        max = substring.size();
            substring.erase(substring.begin(), substring.begin()+substring.find(s[i])+1);
      substring+=s[i];
       
    }
        }
        if(substring.size()>max)
            max = substring.size();
        return max;
    }
};