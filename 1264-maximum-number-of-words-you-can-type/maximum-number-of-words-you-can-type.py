class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        bad = set(list(brokenLetters))
        words = text.split(' ')
        out = 0
        for word in words:
            if set(list(word)).intersection(bad) == set(): 
                out += 1
        return out

