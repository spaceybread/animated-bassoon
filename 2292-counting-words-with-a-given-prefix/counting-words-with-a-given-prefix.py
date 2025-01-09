class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return sum([1 if (s[:len(pref)] == pref) else 0 for s in words])