class Solution {
public:
    string defangIPaddr(string address) {
        int index{};
        string substr = ".";
        while ((index = address.find(substr, index)) != std::string::npos) {
            address.replace(index,1,"[.]");
            index += substr.length()+2;
        }
        return address;
    }
};