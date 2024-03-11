class Solution {
public:
    void duplicateZeros(vector<int>& arr) {
      int zeros{};
  vector<int> indexes{};
  for (int i = 0; i < arr.size(); i++) {
    if (arr[i] == 0) {
      indexes.push_back(i);
    }
  }
  for (int i = 0; i < indexes.size(); i++) {
    arr.insert(arr.begin() + indexes[i] + zeros, 0);
    zeros++;
  }
  arr.resize(arr.size() - zeros);
}};