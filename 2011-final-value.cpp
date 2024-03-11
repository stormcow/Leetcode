class Solution {
public:
    int finalValueAfterOperations(vector<string>& operations) {
        int x{};
        for(string word: operations){
            for(char operat: word){
                if(operat=='+')
                {
                    x++;
                    break;
                }
                else if(operat=='-')
                {
                    x--;
                    break;
                }
            }
        }
        return x;
    }
};