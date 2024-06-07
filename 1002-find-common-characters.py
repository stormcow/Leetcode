class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        chars = defaultdict(int)
        for char in words[0]:
            chars[char] += 1
        for word in words[1:]:
            for key in chars.keys():
                if word.count(key) == chars[key]:
                    continue
                elif word.count(key) < chars[key] and word.count(key) > 0:
                    chars[key] = word.count(key)
                elif word.count(key) == 0:
                    chars[key] = 0
        return [
            keyval[0]
            for keyval in chars.items()
            if keyval[1] > 0
            for _ in range(keyval[1])
        ]
