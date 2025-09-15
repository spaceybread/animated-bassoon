class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        return sum([1 if set(list(word)).intersection(set(list(brokenLetters))) == set() else 0 for word in text.split(' ')])