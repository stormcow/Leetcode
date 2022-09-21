class Solution {
public:
  int lengthOfLastWord(string s) {
    bool isWord{};
    int length{};
    for (int i = s.size() - 1; i >= 0; i--) {
      if (!isspace(s[i]) && !isWord) {
        isWord = true;
        length++;
      } else if (!isspace(s[i]))
        length++;
      else if (isspace(s[i]) && isWord)
        break;
    }
    return length;
  }
};