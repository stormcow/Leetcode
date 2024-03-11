class Solution {
public:
    bool isPalindrome(int x) {
        int n{x};
        int remainder{};
        long int reversed{};
        if(x<0)
            return false;
        while(n!=0){
            remainder = n%10;
            reversed = (reversed * 10) + remainder;
            n/=10;
        }
        if(x==reversed)
            return true;
        return false;
    }
};