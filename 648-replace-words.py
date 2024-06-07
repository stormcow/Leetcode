# slow but works, too lazy to do trie right now :thumbsup:
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        sentences = sentence.split()
        strings = []
        for i in range(len(sentences)):
            min_match = (float("inf"), "")
            for root in dictionary:
                if sentences[i].find(root) == 0:
                    key = (len(root), root)
                    min_match = min(min_match, key, key=lambda x: x[0])
            if min_match[1] == "":
                strings.append(sentences[i])
            else:
                strings.append(min_match[1])
        return " ".join(strings)
