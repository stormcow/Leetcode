#include <algorithm>
#include <iostream>
#include <iterator>
#include <string>
#include <vector>

bool isAnagram(std::string s, std::string t) {
  if (s.size() != t.size())
    return false;

  std::string work = s;

  std::sort(work.begin(), work.end());
  auto it = std::unique(work.begin(), work.end());
  work.resize(std::distance(work.begin(), it));
  std::vector<int> str1{}, str2{};

  for (int i = 0; i < work.size(); i++) {
    str1.push_back(std::count(s.begin(), s.end(), work[i]));
    str2.push_back(std::count(t.begin(), t.end(), work[i]));
  }

  if (str1 != str2)
    return false;

  for (int i = 0; i < s.size(); i++) {
    if (t.find(s[i]) == std::string::npos)
      return false;
  }
  return true;
}

std::vector<std::vector<std::string>>
groupAnagrams(std::vector<std::string> &strs) {
  std::vector<int> indexes{};
  std::vector<std::vector<std::string>> ans{};

  for (int i = 0; i < strs.size(); i++) {
    std::cout << '\n';
    if (std::find(indexes.begin(), indexes.end(), i) != indexes.end())
      continue;
    std::vector<std::string> temp{strs[i]};
    indexes.push_back(i);
    for (int j = 0; j < strs.size(); j++) {
      if (j == i || strs[i].size() != strs[j].size())
        continue;
      if (isAnagram(strs[i], strs[j])) {
        temp.push_back(strs[j]);
        indexes.push_back(j);
      }
    }
    for (auto i : temp)
      std::cout << i;

    ans.push_back(temp);
  }

  return ans;
}

int main() {
  std::vector<std::string> input{"eat", "tea", "ate", "nat", "bat"};
  std::vector<std::vector<std::string>> ans = groupAnagrams(input);

  //  for (int i = 0; i < ans.size(); i++) {
  //    for (int j = 0; j < ans[i].size(); j++)
  //      std::cout << ans[i][j] << ' ';
  //    std::cout << '\n';
  //  }
}