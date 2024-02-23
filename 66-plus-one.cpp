class Solution {
public:
  void increment(std::vector<int> &vec, int index) {
    if (index == 0 && vec[index] == 9) {
      vec[index] = 0;
      vec.insert(vec.begin(), 1);
    } else if (vec[index] == 9) {
      vec[index] = 0;
      increment(vec, index - 1);
    } else
      vec[index]++;
  }
  vector<int> plusOne(vector<int> &digits) {
    increment(digits, digits.size() - 1);
    return digits;
  }
};