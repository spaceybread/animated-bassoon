class Solution:
    def canBeTypedWords(self, text: str, brk: str) -> int:
        brkSet = set(brk)
        c = sum(not set(w) & brkSet for w in text.split())

        return c