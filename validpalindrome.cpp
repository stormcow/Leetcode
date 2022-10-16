#include <string>
#include <algorithm>
#include <cwctype>
#include <cctype>
#include <iostream>

    void convert(std::string& s){
        
        for(int i = 0; i < s.size(); i++){
            if(!iswalnum(s[i]))
                s.erase(s.begin()+i);
            else
                s[i]=std::tolower(s[i]);
        }
        
    }

        bool isPalindrome(std::string s) {
        convert(s);
        std::string b = s;
        std::reverse(b.begin(),b.end());
        if(b==s)
            return true;
        return false;
    }

    int main(){
        std::string s = "A man, a plan, a canal: Panama";

        std::cout<<isPalindrome(s);
    }