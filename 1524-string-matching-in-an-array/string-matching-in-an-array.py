class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=len)
        out = []

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if words[i] in words[j]: 
                    out.append(words[i])
                    break
        
        return out