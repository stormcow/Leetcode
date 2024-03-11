class Solution {
public:
    int mostWordsFound(vector<string>& sentences) {
        int max{};
        string substr{" "};
        
        for(string x: sentences){
            int index{};
            int current{1};
            while((index=x.find(substr, index))!=string::npos)
            {
                index+=substr.size();
                current++;
            }
            if(current>max)
                max=current;
        }
        return max;
    }
};